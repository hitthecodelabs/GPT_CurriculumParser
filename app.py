import os
import json
import openai
import PyPDF2
from flask import Flask, render_template, request, send_from_directory, send_file

app = Flask(__name__)
# UPLOAD_FOLDER = './uploads/'
# DOWNLOAD_FOLDER = './downloads/'

UPLOAD_FOLDER = '/tmp/uploads/'
DOWNLOAD_FOLDER = '/tmp/downloads/'

# Setup the directories
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

openai.api_key = ''

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        json_file_path, json_obj = process_pdf(filename)
        return render_template('download.html', json_file=json_file_path, json_content=json_obj)

@app.route('/download/<filename>', methods=['GET', 'POST'])
def download(filename):
    return send_file(os.path.join(app.config['DOWNLOAD_FOLDER'], filename), as_attachment=True)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

def process_pdf(pdf_path):
    # your provided code here, adjusted to work with the given pdf_path
    pdf_content = ''

    # pdf = pdfs[1]

    # Open the PDF file in read-binary mode
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        # Get the number of pages in the PDF
        num_pages = len(reader.pages)

        # Loop through each page
        for page_num in range(num_pages):
            # print(page_num)
            # Get a specific page
            page = reader.pages[page_num]

            # Extract text from the page
            text = page.extract_text()

            pdf_content+=text

            # print(f"Content from page {page_num + 1}:")
            # print(text)

            if len(pdf_content)>12000:
                break
    file.close()
    
    prompt = (
        ### here you can use your own prompt...
        f""
    )

    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
                                            # model="gpt-3.5-turbo",
                                            model = 'gpt-3.5-turbo-16k',
                                            messages=messages
                                            )

    message = response['choices'][0]['message']['content']
    # print(message)
    
    json_object = json.loads(message)

    # print(json_object)
    
    json_obj = json.dumps(json_object, indent = 3) 
    # print(json_obj)

    # with open("json_cv_extraction.json", "w") as file:
    #     json.dump(json_obj, file)
    # file.close()

    # Saving the JSON to the download directory
    json_file_path = os.path.join(app.config['DOWNLOAD_FOLDER'], 'json_cv_extraction.json')
    with open(json_file_path, "w") as file:
        json.dump(json_obj, file)
    file.close()

    return json_file_path, json_obj

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
