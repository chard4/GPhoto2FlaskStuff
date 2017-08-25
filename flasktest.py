from flask import Flask, url_for, redirect, render_template, send_from_directory
import gphoto2 as gp

import rawpy, imageio

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/takePicture')
def takePicture():
    context = gp.gp_context_new()
    error, camera = gp.gp_camera_new()
    error = gp.gp_camera_init(camera, context)
    capturetype = gp.GP_CAPTURE_IMAGE
    error, path = gp.gp_camera_capture(camera, capturetype, context)
    filetype = gp.GP_FILE_TYPE_NORMAL #http://www.gphoto.org/doc/api/gphoto2-file_8h.html#ab9f339bdf374343272c62d2352753d69
    error, file = gp.gp_camera_file_get(camera, path.folder, path.name, filetype, context)
    error = gp.gp_file_save(file, '/albums/default/'+path.name)
    error = gp.gp_camera_exit(camera, context)
    raw = rawpy.imread(path.name)
    rgb = raw.postprocess()
    convertedName = path.name[0:(path.name.index('.'))] + '.jpg'
    imageio.imwrite(convertedName, rgb)
    #want to redirect to displaying the downloaded image
    return redirect(url_for('displayPicture', id=convertedName))

#can maybe do some kind of routing where you route to the picture with the specific id
@app.route('/displayPicture/<filename>')
def displayPicture(filename):
    return render_template('displayPicture.html',filename=filename)

@app.route('/uploads/<path:filename>')
def download_file(filename):
    return send_from_directory('./', filename, as_attachment=True)

def gallery():
    return 0

if __name__ == '__main__':
    app.run()


'''
so the goal is to have a home page
that has 2 buttons or something
    first is take picture
    second is look at images taken?

so you'd want the button to send you to /takePicture,
which should do the gphoto2 code and then redirect you back to home?
i actually am not sure...
'''