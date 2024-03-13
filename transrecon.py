from flask import Flask, render_template, request
import os
import logging

app = Flask(__name__)

# Set up logging
log_file_path = 'app.log'
logging.basicConfig(filename=log_file_path, level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the files part
        if 'file1' not in request.files or 'file2' not in request.files:
            logger.error('No file part')
            return 'No file part'

        file1 = request.files['file1']
        file2 = request.files['file2']

        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file1.filename == '' or file2.filename == '':
            logger.error('No selected file')
            return 'No selected file'

        if file1 and file2:
            # Here, you can add your logic to handle the uploaded files
            # For example, saving them to a directory:
            # file1.save(os.path.join('/path/to/save', file1.filename))
            # file2.save(os.path.join('/path/to/save', file2.filename))
            # And then compare the Excel files as needed
            return 'Files successfully uploaded and compared'

    # If not a POST request, load the upload form
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
