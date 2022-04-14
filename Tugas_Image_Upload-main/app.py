#Mulyana Putriyani - 6B - 19090113
#Risma Niankupandang - 6D - 19090083

from flask import Flask

UPLOAD_FOLDER = 'C:/Users/lenovo/apiuploadimg/img'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024