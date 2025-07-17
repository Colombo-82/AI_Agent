import os
from google.genai import types


def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot write "{file_path}" as it is outside the permitted working directory'
    try:
        directory_path = os.path.dirname(target_file)
        if directory_path and not os.path.exists(directory_path):
            os.makedirs(directory_path)
        with open(target_file, 'w') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
    

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="overwrite the file with the content provided, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to overwrite. If not provided, say 'File must be provided'.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="A string to overwrite the file.",
            ),
        },
    )
)