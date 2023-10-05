import pandas as pd
import PySimpleGUI as sg
from map_creation import map_creation
from model_training import model_training
from coordinates_input_GUI import coordinates_input_GUI


# Read the CSV file into a pandas DataFrame with the correct encoding
HM_measurements_df = pd.read_csv('HM_small_codenames.csv', encoding= 'UTF-8')

# Convert the DataFrame to a NumPy array
arr = HM_measurements_df.to_numpy()
# Extract the 3rd and 4th columns of the DataFrame
coordinates_df = HM_measurements_df.iloc[:, 2:4]
# Drop all rows that contain NaN values
coordinates_df.dropna(inplace=True)
# Convert the DataFrame to a NumPy array
coordinates_arr = coordinates_df.to_numpy()
# Print the shape of the array
print(coordinates_arr.shape)
# Print the array
print("\n", coordinates_arr)


total_radiation = HM_measurements_df.iloc[:, 0]
total_radiation_arr = total_radiation[total_radiation.notnull()].tolist()
print("\n",total_radiation_arr)


# gui = coordinates_input_GUI()
# location = gui.get_location()
def get_location():
    gui = coordinates_input_GUI()
    gui.window.mainloop()
    return gui.location

if __name__ == "__main__":
    location = get_location()


#calling the training model file
model_trainer = model_training(HM_measurements_df,HM_measurements_df, location)
prediction = model_trainer.train_model()
#print(prediction)


#calling map_creation.py constructor
map_creator = map_creation(location, coordinates_arr, prediction)
map_creator.create_map()























