from flask import Flask, render_template,request
import os,io
from google.cloud import vision
from google.cloud.vision import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'account_key.json'
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['inputFile']
    f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(f)
  
    client = vision.ImageAnnotatorClient()
    file_name = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    to_return = dict()
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
        to_return[file_name]=content

    image = types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))
        output='\n"{}"'.format(text.description)
        return render_template('success.html',output=output)

if __name__ == '__main__':
    app.run(debug=True)
