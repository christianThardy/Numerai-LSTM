
# Dependencies
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
import numpy as np
import pandas as pd
import keras

def main():
    # Set seed for reproducibility
    np.random.seed(0)

    print("Loading data...")
    # Load the data from the CSV files
    training_data = pd.read_csv('numerai_training_data.csv', header=0)
    prediction_data = pd.read_csv('numerai_tournament_data.csv', header=0)
    
    X = training_data.iloc[:, 3:52].values
    Y = training_data.iloc[:, 53:54].values
    P = prediction_data.iloc[:, 3:52].values
    ids = prediction_data["id"]
    
    # Creating a data structure with 120 timesteps and 1 output
    X_train = []
    Y_train = []
    for i in range(360, 393613): 
        X_train.append(X[i-360:i, 0])
        Y_train.append(Y[i, 0])
        X_train, Y_train = np.array(X_train), np.array(Y_train)
        # Reshaping
        X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
    
    # Network initialization  
    regressor = Sequential()
    # First layer w/ dropout
    regressor.add(LSTM(units = 85, return_sequences = True, input_shape = (X_train.shape[1], 1)))
    regressor.add(Dropout(0.2))
    # Second layer w/ dropout
    regressor.add(LSTM(units = 85, return_sequences = True))
    regressor.add(Dropout(0.2))
    # Third layer w/ dropout
    regressor.add(LSTM(units = 85, return_sequences = True))
    regressor.add(Dropout(0.2))
    # Fourth layer w/ dropout
    regressor.add(LSTM(units = 85))
    regressor.add(Dropout(0.2))
    # Output layer & activation function
    regressor.add(Dense(units = 1, activation = 'linear'))
    # Compile lstm-rnn
    regressor.compile(keras.optimizers.Adam(lr=0.002, beta_1=0.9, beta_2=0.999, decay = -0, 
                                       amsgrad = False), loss = 'mean_squared_error', metrics = ['accuracy'])
                                              
    regressor.summary()       
    # Loss and other metrics recorded at the end of each epoch
    history = regressor.fit(X, Y, epochs = 1, batch_size = 32, validation_split = 0.05) # callbacks = callbacks_list
    # Keys that allow training and validation set to evaluate 
    # The optimized loss of fitting to the model
    print(history.history['loss'])
    print(history.history['val_loss'])
    
    
    print("Training...")
    # Model is fit to the training data
    regressor.fit(X, Y)

    print("Predicting...")
    # The trained model is used to make predictions on the numerai_tournament_data
    # The model returns two columns: [probability of 0, probability of 1]
    # Only interested in the probability that the target is 1.
    y_prediction = regressor.predict_proba(P)
    results = y_prediction[:, 1]
    results_df = pd.DataFrame(data={'probability':results})
    joined = pd.DataFrame(ids).join(results_df)

    print("Writing predictions to predictions.csv")
    # Save the predictions out to a CSV file
    joined.to_csv("predictions.csv", index=False)
    # Upload predictions on numer.ai


if __name__ == '__main__':
    main()