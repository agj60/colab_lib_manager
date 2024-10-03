# colab_lib_manager

'colab_lib_manager' is a Python package designed to manage the installation of Python libraries in Google Colab notebooks using Google Drive por persistent storage. It avoids long reinstallation times when re-connecting runtimes.

## Features

- Automatically check if libraries are already installed in the Colab runtime
- Mount Google Drive if necessary and check for libraries stores in a specific folder
- If folder does not exist, create it on Google Drive
- If the library is not available, install it into the folder

## Installation

Install the package using 'pip' directly from GitHub:

    !pip install git+https://github.com/agj60/colab_lib_manager.git

## Usage

```python
from colab_lib_manager import install_libraries
# install libraries in 'colab_libs', a default directory on Google Drive; it can be any
install_libraries(['library_1', 'library_2'], where = 'colab_libs') 
import library_1, library_2
```

