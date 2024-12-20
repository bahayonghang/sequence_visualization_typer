import subprocess

def build():
    """
    Build the main.py script into an executable using Nuitka.
    """
    try:
        # Run the Nuitka command to compile main.py into an executable
        subprocess.run([
            "python", "-m", "nuitka",
            "--standalone",
            "--onefile",
            "--output-dir=dist",
            "main.py"
        ], check=True)
        print("Build successful. The executable is located in the 'dist' directory.")
    except subprocess.CalledProcessError as e:
        print(f"Build failed: {e}")

if __name__ == "__main__":
    build()
    