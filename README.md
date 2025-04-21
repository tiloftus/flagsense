FlagSense

![Alt text](relative%20images/logo.png?raw=true "Title")

FlagSense is a Python package for detecting and classifying flags in images. Using advanced computer vision techniques, FlagSense identifies national flags and determines which country they belong to. FlagSense uses state-of-the-art models to detect flags in real-world contexts and accurately classify them by country. 

Installation

FlagSense can be easily installed via pip:
\\ pip install flagsense

Usage

After installation, FlagSense can be easily used in the command line by running the following code, where image_path is a filepath to an image on a local machine.
\\ flagsense image_path

The --model flag allows the user to choose from a list of models included in the package. The default model (if no value is input) is a custom YOLOv8 model trained on all nation flags. The user can choose additional models if they prefer, or can choose continent-specific models. Continent specific models are useful in situations where the user may know the location of an image and thus expect certain nation flags, or is only interested in classifying flags of a certain continent. A list of models and the flags to call them is below:
v8 - YOLOv8, all countries
v9 - YOLOv9, all countries
v10 - YOLOv10, all countries

Interpreting/Exporting Output (Format)

Supported Countries and Flags

(probably link to external page)

License
