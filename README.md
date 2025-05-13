# JS_hunter

To implement "JSIntelliHawk," we will break the project into manageable components. Below is a step-by-step plan for building the CLI and Web-based tool:

Step 1: Core Scanner (Backend)
Create a Python CLI tool to parse JavaScript files, extract endpoints, and flag vulnerabilities.
Integrate Retire.js for detecting vulnerable libraries via subprocess calls.
Use BeautifulSoup for parsing and extracting URLs, endpoints, and variables.
Integrate SecretFinder (modded) for detecting sensitive data leaks.
Add jsbeautifier for prettifying minified JavaScript.
Export findings in JSON format.

Step 2: REST API Backend (Optional)
Use Flask to expose the core scanner as a REST API.
Add endpoints for uploading JavaScript files, triggering scans, and retrieving results.

Step 3: Web GUI (Optional)
Build a React.js frontend for visualizing findings.
Use D3.js for endpoint mapping and token leak visualization.
Style the UI with Tailwind CSS for a sleek, minimal design.
Use Socket.io for real-time interaction with the backend.

Step 4: Storage (Optional)
Use SQLite to store historical scans, token matches, and configurations.
Optionally integrate Redis for task queues if scaling is required.

Step 5: Bonus Features
Add an auto-crawler to enumerate .js links from target domains.
Implement a plugin system for custom rules.
Create a browser extension for scanning JavaScript on visited sites.
Add GraphQL endpoint detection.
Implement auto-validation for keys (e.g., Firebase, AWS) using OSINT.

/home/parrot/Documents/JS_hunter/
├── core_scanner/
│   ├── scanner.py
│   ├── retirejs_wrapper.py
│   ├── secretfinder_wrapper.py
│   ├── utils.py
│   └── __init__.py
├── web_gui/
│   ├── backend/
│   │   ├── app.py
│   │   ├── models.py
│   │   └── utils.py
│   ├── frontend/
│   │   ├── src/
│   │   │   ├── components/
│   │   │   ├── pages/
│   │   │   ├── App.js
│   │   │   └── index.js
│   │   └── public/
│   └── package.json
├── tests/
│   ├── test_scanner.py
│   ├── test_retirejs.py
│   ├── test_secretfinder.py
│   └── test_web_gui.py
└── README.md

## Usage

### Core Scanner (CLI)
1. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the core scanner on a JavaScript file:
   ```bash
   python core_scanner/scanner.py <path_to_js_file> --output <output_json_file>
   ```
   Example:
   ```bash
   python core_scanner/scanner.py example.js --output report.json
   ```

### REST API Backend
1. Install Flask:
   ```bash
   pip install flask
   ```
2. Start the Flask server:
   ```bash
   python web_gui/backend/app.py
   ```
3. Use a tool like `curl` or Postman to upload a JavaScript file for scanning:
   ```bash
   curl -X POST -F "file=@example.js" http://127.0.0.1:5000/scan
   ```

### Web GUI
1. Navigate to the `web_gui` directory:
   ```bash
   cd web_gui
   ```
2. Install frontend dependencies:
   ```bash
   npm install
   ```
3. Start the React development server:
   ```bash
   npm start
   ```
4. Open your browser and navigate to `http://localhost:3000`.

### Testing
1. Run the test suite:
   ```bash
   pytest tests/
   ```

### Notes
- Ensure `Retire.js` and `SecretFinder` are installed and accessible in your system's PATH.
- For `Retire.js`, install it globally using npm:
  ```bash
  npm install -g retire
  ```
- For `SecretFinder`, clone the repository and ensure the script is executable:
  ```bash
  git clone https://github.com/m4ll0k/SecretFinder.git
  cd SecretFinder
  pip install -r requirements.txt
  ```