# colab_lib_manager

'colab_lib_manager' is a Python package designed to manage the installation of Python libraries in Google Colab notebooks using Google Drive por persistent storage. It avoids long reinstallation times when re-connecting runtimes.

## Features

- Automatically check if libraries are already installed in the Colab runtime
- Mount Google Drive if necessary and check for libraries stores in a specific folder
- If the library is not available, install it into Google Drive

## Instalation

Clone the repository and install the package using 'pip', placing these 2 lines in a Colab cell:

    ```
    !git clone https://github.com/agj60/colab_lib_manager.git
    !pip install -e colab_lib_manager/
    ```

## Usage

```python
from colab_lib_manager import install_libraries
install_libraries(['library_1', 'library_2'])
import library_1, library_2
```

