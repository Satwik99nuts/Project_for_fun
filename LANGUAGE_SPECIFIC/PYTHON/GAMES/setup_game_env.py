import importlib
import subprocess
import sys

# List of required packages for Python game development
packages = [
    "pygame",
    "arcade",
    "numpy",
    "Box2D",
    "pydub",
    "ursina",
    "panda3d",
    "PyOpenGL",
    "PyOpenGL_accelerate"
]

def install_package(package):
    """Install a package using pip"""
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package])

def check_and_install(packages):
    for package in packages:
        try:
            importlib.import_module(package.lower())
            print(f"✅ {package} is already installed.")
        except ImportError:
            print(f"📦 Installing {package}...")
            install_package(package)

if __name__ == "__main__":
    print("🔍 Checking your Python game dev environment...")
    check_and_install(packages)
    print("\n🎮 All done! You’re ready for game development in Python.")
