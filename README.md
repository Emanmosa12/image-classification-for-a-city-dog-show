# Image Classification for a City Dog Show

An image classification project developed as part of the **Udacity AI Programming with Python Nanodegree**.

## Project Overview

This project develops an image classification pipeline for a city dog show application. The program analyzes images of pets, identifies whether an image contains a dog, and predicts the dog's breed when applicable.

The project combines image processing, deep learning, and performance evaluation to build a practical image classification workflow.

## Objectives

The main objectives of the project are to:

* Process and label pet images from a dataset.
* Determine whether each image contains a dog.
* Classify images using pretrained convolutional neural network (CNN) models.
* Compare predicted labels with the expected labels.
* Calculate classification statistics and evaluate model performance.
* Test the classifier using additional uploaded images.

## Technologies

* Python
* PyTorch
* Convolutional Neural Networks (CNNs)
* Pretrained deep learning models
* Image classification
* Data processing and evaluation

## Models

The project evaluates pretrained CNN architectures for image classification, including:

* **AlexNet**
* **VGG**
* **ResNet**

These pretrained models are used to classify images and identify dog breeds.

## Project Workflow

The project follows a structured image-classification pipeline:

1. **Parse input arguments**
   Configure the image directory, model architecture, and other project options.

2. **Extract image labels**
   Process image filenames and extract the expected pet labels.

3. **Classify images**
   Use pretrained CNN models to predict the class of each image.

4. **Identify dogs**
   Determine whether the predicted class represents a dog.

5. **Compare results**
   Compare the model predictions with the expected labels.

6. **Calculate statistics**
   Evaluate the performance of the classifier for dog and breed classification.

7. **Test uploaded images**
   Run the classifier on additional images to demonstrate its practical use.

## Project Structure

```text
image-classification-for-a-city-dog-show/
│
├── pet_images/
│   └── Pet image dataset
│
├── uploaded_images/
│   ├── cat_01.jpg
│   ├── Dog_01.jpg
│   ├── Dog_02.jpg
│   └── Pen_01.jpg
│
├── adjust_results4_isadog.py
├── calculates_results_stats.py
├── check_images.py
├── classifier.py
├── classify_images.py
├── dognames.txt
├── get_input_args.py
├── get_pet_labels.py
├── imagenet1000_clsid_to_human.txt
├── print_functions_for_lab_checks.py
├── print_results.py
└── test_classifier.py
```

## Key Components

### `classifier.py`

Provides the image classification functionality using pretrained CNN architectures.

### `get_pet_labels.py`

Extracts expected pet labels from the image filenames.

### `classify_images.py`

Runs image classification using the selected pretrained model.

### `adjust_results4_isadog.py`

Determines whether the expected and predicted labels correspond to dogs.

### `calculates_results_stats.py`

Calculates statistics used to evaluate classification performance.

### `print_results.py`

Formats and displays the classification results and performance statistics.

## Results & Evaluation

The project evaluates the classifier using several measures, including:

* Correct dog classification
* Correct non-dog classification
* Correct dog-breed classification
* Incorrect classifications
* Overall classification performance

The evaluation allows different pretrained CNN architectures to be compared based on their performance on the pet image dataset.

## How to Run

The project can be executed from the command line by providing the required image directory and model architecture.

Example:

```bash
python classify_images.py
```

The project can also be tested using the uploaded images in the `uploaded_images/` directory.

## Learning Outcomes

Through this project, I gained practical experience with:

* Python-based image processing
* Deep learning and CNN-based image classification
* Using pretrained models with PyTorch
* Comparing model predictions with expected labels
* Evaluating machine learning model performance
* Structuring a machine learning project into reusable Python modules
* Testing image classification models on new images

## Program

**AI Programming with Python Nanodegree — Udacity**

This project was completed as part of my AI Programming with Python Nanodegree studies.

## Author

**Eman Mousa**

Computer Science graduate | MScFE student | Data Science & Machine Learning

---

*This repository contains my implementation and project work completed during the Udacity AI Programming with Python Nanodegree.*
