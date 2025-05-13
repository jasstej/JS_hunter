from flask import Flask, request, jsonify
from core_scanner.scanner import scan_js_file

app = Flask(__name__)

@app.route('/scan', methods=['POST'])
def scan_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    
    file = request.files['file']
    file_path = f"/tmp/{file.filename}"
    file.save(file_path)
    
    # Run the scanner
    results = scan_js_file(file_path)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
