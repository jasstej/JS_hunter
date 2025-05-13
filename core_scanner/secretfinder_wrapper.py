import subprocess

def run_secretfinder(file_path):
    """
    Run SecretFinder on the given JavaScript file to detect sensitive data leaks.
    """
    try:
        result = subprocess.run(
            ["python3", "SecretFinder.py", "-i", file_path, "-o", "cli"],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            raise Exception(f"SecretFinder error: {result.stderr}")
        
        # Return raw output for further processing
        return result.stdout
    except Exception as e:
        print(f"Error running SecretFinder: {e}")
        return None
