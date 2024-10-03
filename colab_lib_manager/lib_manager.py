import sys
import subprocess
import os
from importlib import import_module
from google.colab import drive
def install_libraries(libraries, where = 'colab_libs'):
  """
  PIP Install libraries in Google Drive for use in Google Colab.
  Args:
    libraries: str or list of str
    where: str
  """

  # Ensure libraries is a list
  if isinstance(libraries, str):
    libraries = [libraries]

  # Mount Google Drive if it isn't already mounted
  if not os.path.exists('/content/drive'):
    print("Mounting Google Drive...")
    drive.mount('/content/drive', force_remount=True)

  # Path where libraries will be installed in Google Drive
  drive_lib_path = '/content/drive/MyDrive/' + where

  # Make sure the custom folder exists in Google Drive
  if not os.path.exists(drive_lib_path):
    print("Creating custom folder in Google Drive...")
    os.makedirs(drive_lib_path)

  if not sys.path.__contains__(drive_lib_path):
    sys.path.append(drive_lib_path)

  for lib in libraries:
    try:
      import_module(lib) # Only checks whether library is installled, do not load it
      print(f"{lib} already installed")
    except ImportError:
      # If not installed, install it on Google Drive
      print(f"Installing {lib} on Google Drive...")
      subprocess.check_call([sys.executable, "-m", "pip", "install", lib, "-t", drive_lib_path,"--ignore-installed"])
      try:
        import_module(lib) # Only checks whether library is installled, do not load it
        print(f"{lib} installed in Google Drive")
      except ImportError:
        print(f"Error installing {lib}. Please install it manually.")
