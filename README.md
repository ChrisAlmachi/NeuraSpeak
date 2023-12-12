
  NEURASPEAK 

This repository presents the development of an English language learning tool called NeuraSpeak. This tool combines the detection of audio to identify grammatical errors and the generation of vocabulary for learning. In addition, it can generate evaluations with their corresponding grade. Moreover, the code was brought to classrooms, making it more modular, reusable, and easy to maintain. Finally, we present a Domain-specific language (DSL) proposal using NeuraSpeak. This implementation allows us to offer an efficient solution that addresses various challenges associated with text correction and English learning.


VERSION = '1.0.0' 
PACKAGE_NAME = 'NeuraSpeak' 
AUTHOR = 'Christopher Almachi and David Carlosama' 
AUTHOR_EMAIL = 'christopher.almachi@yachaytech.edu.ec, david.carlosama@yachaytech.edu.ec'
URL = '[https://github.com/](https://github.com/ChrisAlmachi/NeuraSpeak.git)'

LICENSE = 'Open-Source' #Tipo de licencia
DESCRIPTION = 'Library for identifying, recognizing errors, learning English language vocabulary and vocabulary'
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8') 
LONG_DESC_TYPE = ""


INSTALL_REQUIRES = [
    'nltk',
    'language_tool_python',
    'numpy',
    'speech_recognition',
    'nltk.tokenize',
    'nltk.corpus',
    'random'
      ]


You need to install
    - java

After that, you need to ejecute all step in ipynb file or ejecute class file
