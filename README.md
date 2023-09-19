# Predictive-Learning
This is the project for predictive learning

##### Data source: https://data.mendeley.com/datasets/4drtyfjtfy/1 
we download the file and name it as `dataset`

# Description

## Step
1. To preprocess the data, the `data_split.py` program categorizes the image files located in the `dataset` folder and moves them to the `./data/weather_dataset` directory.
2. Build The Model: `main.py` splits the image files into random forest classifier, test how the performance is, and save the model as `model.p`
3. Build The Model: load the model we save and pick the random image to test if the model can predict what image it feeds.

## Data Preprocessing

1. Defines the paths for the source dataset (`DATA_PATH`) and the target dataset (`TARGET_PATH`) where the images will be sorted and moved.
2. Specifies the dataset's desired train-validation split ratio (`RATIO`).
3. Define the categories of the images.
4. Create the necessary subdirectories within the train and validation folders based on the categories.
5. Retrieve each category's image files using the `glob` function and shuffle them randomly.
6. Determines the split point based on the specified ratio and separates the files into train and validation sets.
7. Move the train files to the corresponding category subdirectory within the train folder.
8. Move the validation files to the corresponding category subdirectory within the validation folder.

In summary, the code takes a dataset of images and organizes them into a train-validation split based on the specified ratio. It creates the necessary folder structure and moves the images into their respective category subdirectories within the train and validation folders.


## Build The Model
The code performs the following steps:

1. Imports necessary libraries and modules: `os`, `pickle`, `img2vec_pytorch`, `PIL`, `sklearn.ensemble`, and `sklearn.metrics`.
2. Initializes an `Img2Vec` object from the `img2vec_pytorch` library.
3. Defines the directory paths for the training and validation data.
4. Creates an empty dictionary called `data` to store the features and labels of the training and validation data.
5. Iterates over the training and validation directories to extract features and labels from the images.
6. Converts each image to RGB format using the `PIL` library.
7. Extracts the image features using the `Img2Vec` object.
8. Appends the image features and labels to the respective lists.
9. Stores the features and labels in the `data` dictionary.
10. Initializes a `RandomForestClassifier` model with a random state of 0.
11. Trains the model using the training data and labels.
12. Predicts the labels for the validation data using the trained model.
13. Calculates the accuracy score of the model by comparing the predicted labels with the actual labels.
14. Prints the accuracy score.
15. Saves the trained model as a pickle file named `model.p`.
### The accuracy code we test is: 0.9646017699115044

This code aims to train a random forest classifier on a weather dataset. The dataset is divided into training and validation sets. The code uses the `Img2Vec` library to extract features from the images and then trains a `RandomForestClassifier` model on the extracted features. The accuracy of the model is then calculated and printed. Finally, the trained model is saved as a pickle file for future use.


## Test how the model works

1. The code imports the necessary libraries and modules: `img2vec_pytorch`, `PIL`, and `pickle`.
2. It opens the saved model file (`model.p`) using the `pickle.load()` function and assigns it to the `model` variable.
3. It creates an `Img2Vec` object called `img2vec`.
4. It specifies the path of an image (`img_path`) that will be used for prediction.
5. It opens the image using the `Image.open()` function from the `PIL` library and assigns it to the `img` variable.
6. It extracts the features of the image using the `get_vec()` method of the `img2vec` object and assigns them to the `features` variable.
7. It predicts the label of the image by passing the `features` to the `predict()` method of the `model` object and assigns the result to the `pred` variable.
8. It prints the predicted label.

This code uses a pre-trained model (`model.p`) and the `Img2Vec` library to extract features from an image (`img_path`). It then uses the trained model to predict the label of the image and prints the predicted label.



