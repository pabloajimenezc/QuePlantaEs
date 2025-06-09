from pathlib import Path
import subprocess
import sys

packages_list = ['Pillow', 'matplotlib', 'numpy']

for package in packages_list:
    print(f"Installing {package}...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])