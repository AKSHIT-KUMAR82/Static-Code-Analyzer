def read_code(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return []
