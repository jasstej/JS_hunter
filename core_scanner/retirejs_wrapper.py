import subprocess
import json

def run_retirejs(file_path):
    """
    Run Retire.js on the given JavaScript file to detect vulnerable libraries.
    """
    try:
        result = subprocess.run(
            ["retire", "--outputformat", "json", "--input", file_path],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            raise Exception(f"Retire.js error: {result.stderr}")
        
        # Parse JSON output
        return json.loads(result.stdout)
    except Exception as e:
        print(f"Error running Retire.js: {e}")
        return None
