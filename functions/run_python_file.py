import os
import subprocess


def run_python_file(working_directory, file_path, args=None):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(target_file):
        return f'Error: File "{file_path}" not found.'
    if not target_file.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        result = subprocess.run(['python', target_file], capture_output=True, timeout=30, text=True, cwd=working_directory)
        output = f"STDOUT:{result.stdout}\nSTDERR:{result.stderr}"
        if result.returncode != 0:
            output += f"\nProcess exited with code {result.returncode}"
        if not result.stdout.strip() and not result.stderr.strip():
            output = "No output produced."
        return output
    except Exception as e:
        return f"Error: executing Python file: {e}"
    