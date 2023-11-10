# Plant Disease Detection using CNN

This repository contains an implementation of plant disease detection using a Convolutional Neural Network (CNN) built from scratch. The repository also contains a web app allowing users to upload an image of a plant and the CNN model predicts whether the plant is healthy or if it is affected by powdery mildew or rust.

---

### NOTE: 

I was unable to upload the weight files because of a Git LFS problem (repository exceeded its data quota. 😔)
However if you still wish to download the weights, you can do that using this [link](https://www.mediafire.com/file/1j3dwd2pzs7xc13/weights.rar/file). 👍

---

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Model](#model)
- [License](#license)
 <!--- - [Demo](#demo) --->

## Introduction

Plant diseases can have a detrimental impact on crop yield. Early detection and intervention are crucial to prevent the spread of diseases and minimize damage. The Streamlit web application provides an easy-to-use interface for users to upload plant images, which are then processed using a CNN model to predict the health status of the plant.

## Prerequisites

Before running the application, make sure you have the following dependencies installed:

- Python 3.x
- TensorFlow
- Streamlit
- Numpy
- Pillow (PIL)
- The model weights file (`plant_disease_classifier.h5`) should be available in the `weights` directory.

You can install the required packages using `pip`:

```bash
pip install tensorflow streamlit numpy pillow
```

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/arpy8/Plant_Disease_Detection.git
   cd Plant_Disease_Detection_using_CNN
   ```

2. Place the model weights file (`plant_disease_classifier.h5`) in the `weights` directory.

3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

4. The web app will open in your default web browser, allowing you to upload plant images for disease classification.

## File Structure
```
├── LICENSE
├── README.md          <- The top-level README for developers/collaborators using this project.
├── app.py             <- Source Code for the streamlit web app hosted by me.
│
└── assets             <- Folder containing the assets for the web app
│   ├── bg.png         <- Background image
│   ├── logo.png       <- Logo image
│   └── sample         <- Contains random image from the dataset for the web app
│
│
├── notebook           <- Folder containing the notebook used for training the CNN model
│   └── Plant-Disease-Detection-using-CNN.ipynb      <- Contains the model weights
│
└── weights            <- Folder containing the dataset reports/results of this project
    └── plant_disease_classifier.h5                  <- Model weights of the cnn model

```

## Model

The model used for plant disease classification is a CNN model. It has been trained to classify plants into one of the following categories:
- Healthy
- Powdery
- Rust

The model's architecture and weights are loaded from the `plant_disease_classifier.h5` file.

<!---
## Demo

To see a live demo of the web app, you can visit [this link](https://your-demo-link-here).
--->

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
