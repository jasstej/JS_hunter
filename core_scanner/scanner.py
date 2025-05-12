import os
import re
import json
import jsbeautifier
from bs4 import BeautifulSoup

def extract_endpoints(js_content):
    # Regex to extract URLs and endpoints
    urls = re.findall(r'https?://[^\s"\']+', js_content)
    return urls

def detect_sensitive_data(js_content):
    # Regex to detect sensitive patterns like API keys, tokens, etc.
    patterns = {
        "apikey": r'apikey\s*[:=]\s*[\'"][a-zA-Z0-9-_]+[\'"]',
        "token": r'token\s*[:=]\s*[\'"][a-zA-Z0-9-_]+[\'"]',
        "secret": r'secret\s*[:=]\s*[\'"][a-zA-Z0-9-_]+[\'"]'
    }
    matches = {}
    for key, pattern in patterns.items():
        matches[key] = re.findall(pattern, js_content)
    return matches

def detect_insecure_patterns(js_content):
    # Detect usage of insecure functions like eval() and Function()
    patterns = {
        "eval": r'\beval\s*\(',
        "Function": r'\bFunction\s*\('
    }
    matches = {}
    for key, pattern in patterns.items():
        matches[key] = re.findall(pattern, js_content)
    return matches

def prettify_js(js_content):
    # Use jsbeautifier to prettify minified JavaScript
    return jsbeautifier.beautify(js_content)

def scan_js_file(file_path):
    with open(file_path, 'r') as f:
        js_content = f.read()
    
    # Prettify JS
    pretty_js = prettify_js(js_content)
    
    # Extract endpoints
    endpoints = extract_endpoints(pretty_js)
    
    # Detect sensitive data
    sensitive_data = detect_sensitive_data(pretty_js)
    
    # Detect insecure patterns
    insecure_patterns = detect_insecure_patterns(pretty_js)
    
    # Compile results
    results = {
        "endpoints": endpoints,
        "sensitive_data": sensitive_data,
        "insecure_patterns": insecure_patterns
    }
    return results

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="JSIntelliHawk Core Scanner")
    parser.add_argument("file", help="Path to the JavaScript file to scan")
    parser.add_argument("--output", help="Path to save the JSON report", default="report.json")
    args = parser.parse_args()

    # Run the scanner
    results = scan_js_file(args.file)

    # Save results to JSON
    with open(args.output, 'w') as f:
        json.dump(results, f, indent=4)
    print(f"Scan complete. Results saved to {args.output}")
