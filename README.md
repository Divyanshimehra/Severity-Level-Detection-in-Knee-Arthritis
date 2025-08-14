# Severity-Level-Detection-in-Knee-Arthritis
A CNN-based model for detecting the severity of a patient's medical condition by analyzing his/her X-ray image. Implemented the CNN model in an application developed using Python.

Developed this project in 2023 during my 1st semester of Masters.  

Later I had the honor of presenting my research paper on "Detecting Severity Level of Knee Osteoarthritis using CNN" at the 15th International Conference on Computing, Communication and Networking Technologies (ICCCNT'24), held at Indian Institute of Technology, Mandi.
The research paper got published in Scopus indexed IEEE ICCCNT conference as well.

Read the paper here: https://ieeexplore.ieee.org/document/10724941

The dataset i used : https://data.mendeley.com/datasets/t9ndx37v5h/1

Methodology used for Project Development:
A CNN architecture was designed and implemented using the TensorFlow and Keras libraries.
The trained model was saved and deployed using Flask on a web server, enabling real-time prediction of arthritis severity from user-uploaded knee X-ray images. 

Technology used for Project Development:
Front-End: HTML, CSS
Machine Learning and Web Development: Python 
Framework: Flask

STEPS:
1. Loading Dataset and Preprocessing:
The first step was to obtain a large knee X-ray dataset from Mendeley. The collection included images of knee arthritis at several phases, each with a different severity level. To speed up the analysis, the images were grayscaled and resized to a consistent dimension of 256x256 pixels. 

2. Model Development:
The CNN model was implemented utilizing TensorFlow and Keras libraries, renowned for their efficiency in building deep learning models.

3. Training and Evaluation:
The model underwent rigorous training using a subset of the dataset. The training process encompassed numerous epochs to optimize the model's weights and biases for accurate arthritis severity prediction.

4. Deployment using Flask:
A pivotal aspect of the project involved deploying the trained model into a user-friendly interface using Flask, a Python-based web framework. The Flask application facilitated real-time predictions of knee arthritis severity from user-uploaded X-ray images.
