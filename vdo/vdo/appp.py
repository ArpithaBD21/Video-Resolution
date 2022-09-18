from flask import Flask,request, url_for, redirect, render_template
import os
import sys
import urllib.request
import ffmpeg
from werkzeug.utils import secure_filename
from conf import sample_input,sample_output
from moviepy.editor import *

src_path=os.path.join(sample_input,'vedio.mp4')

# Define a flask app
app = Flask(__name__)


#first file 
@app.route('/')
def hello_world():
    return render_template('Plant.html') #fil to home page

@app.route('/log', methods=['POST','GET'])
def convert():
    '''file = request.files['file']  
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))'''


    return render_template('page1.html') #file to upload the data


@app.route('/back')
def back():
    return render_template('plant.html') #file to upload the data


'''clip = VideoFileClip(src_path)
 
# getting subclip
clip1 = clip.subclip(0, 30)
 
# getting width and height of clip 1
w1 = clip1.w
h1 = clip1.h
 
print("Width x Height of clip 1 : ", end = " ")
print(str(w1) + " x ", str(h1))
 
print("---------------------------------------")
 
# resizing video downsize 50 %
clip2 = clip1.resize(0.5)
 
# getting width and height of clip 1
w2 = clip2.w
h2 = clip2.h
 
print("Width x Height of clip 2 : ", end = " ")
print(str(w2) + " x ", str(h2))
 
print("---------------------------------------")
 
# showing final clip
clip2.ipython_display()


#filep = 'C:/vedio/static/uploads/vedio.mp4'

 
 #loading video gfg'''


if __name__ == '__main__':
    app.run(debug=True)






'''sys.path.append(r'')

stream=ffmpeg.input('vedio.mp4')
stream=stream.filter('fps',fps=5,round='up').filter('scale',w=128,h=128)
strem=ffmpeg.output(stream,'output.mp4')

ffmpeg.run(stream)'''
'''UPLOAD_FOLDER = 'static/uploads/'
import ffmpeg
filep = '/path/to/my/file.mp4'
stream = ffmpeg.input(filep)

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024



import sys
import zlib

with open('Some_Video.mp4', 'rb') as f:
    original_data = f.read()
    original_size = sys.getsizeof(original_data)

compress_data = zlib.compress(original_data, level=5)
compressed_size = sys.getsizeof(compress_data)

print(original_size)
print(compressed_size)'''




if __name__ == '__main__':
    app.run(debug=True)
s