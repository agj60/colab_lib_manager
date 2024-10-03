from setuptools import setup #, find_packages

setup(
    name = 'colab_lib_manager',
    version = '0.1.0',
    description = 'A library to manage installation of Python packages in Google Colab using Google Drive',
    #long_description = open('READ.md').read(),
    #long_description_content_type = 'text/markdown',
    #author = 'agj60',
    #url = 'https://github.com/agj60/colab_lib_manager',
    #packages = find_packages(),
    install_requires = [
        'sys', 'subprocess', 'os', 'importlib', 'google.colab',
    ],
)