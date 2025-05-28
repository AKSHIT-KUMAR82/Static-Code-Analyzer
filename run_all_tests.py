import os
import subprocess

FOLDER = "Inefficient C Files"

def main():
    # Get all .c files in the folder
    c_files = [f for f in os.listdir(FOLDER) if f.endswith(".c")]

    if not c_files:
        print(f"No C files found in '{FOLDER}'")
        return

    for c_file in c_files:
        full_path = os.path.join(FOLDER, c_file)
        print(f"\n{'='*80}")
        print(f"Analyzing file: {full_path}")
        print(f"{'='*80}\n")

        # Run codeguardian.py on the file
        # Make sure Python is the same version and in PATH
        result = subprocess.run(
            ["python", "codeguardian.py", full_path],
            capture_output=True,
            text=True
        )

        print(result.stdout)
        if result.stderr:
            print("Errors:")
            print(result.stderr)

if __name__ == "__main__":
    main()
