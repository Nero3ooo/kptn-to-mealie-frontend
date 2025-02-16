import os
from flask import Flask, render_template, request, send_file
import subprocess
import requests

app = Flask(__name__, static_folder='static', static_url_path="/static")

@app.route('/manifest.json')
def serve_manifest():
    return send_file('manifest.json', mimetype='application/manifest+json')

@app.route('/sw.js')
def serve_sw():
    return send_file('sw.js', mimetype='application/javascript')

@app.route('/', defaults={'path': ''})
@app.route('/execute', methods=['GET'])
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute():
    short_url = request.form['textfield']
    if(short_url == ''):
        result = 'no url'
        return render_template('index.html', result=result)
    try:
        # Resolve the short URL to get the final URL
        response = requests.get(short_url, allow_redirects=True)
        long_url = response.url
        # Extract the last path segment of the long URL
        last_path_segment = long_url.split('/')[-1]
        last_path_segment = last_path_segment.split('?')[0]
        # Run the terminal command

        result = subprocess.check_output(['kptncook', 'search-by-id', last_path_segment], universal_newlines=True)
        result = subprocess.check_output(['kptncook', 'sync-with-mealie'], universal_newlines=True)
        result = 'successfully imported '
    except subprocess.CalledProcessError as e:
        result = f"An error occurred: {e.output}"
    result = result + last_path_segment
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

