from sklearn.tree import DecisionTreeRegressor

class model_training:
    def __init__(self, X, y, location):
        self.X = X
        self.y = y
        self.location = location
        print("The dataset for self.X that enters the model_training.py is \n",self.X)
        print("The dataset for self.Y that enters the model_training.py is \n",self.y)

    def train_model(self):
        # Split the dataset into input and target variables
        X = self.X.drop(columns=['Total_Radiation(75-3000Hz)' ,'Location_Code_Name'])
        y = self.y['Total_Radiation(75-3000Hz)']

        # Train the model
        model = DecisionTreeRegressor()
        model.fit(X, y)

        # Make a prediction
        prediction = model.predict([self.location])
        print('\n\nThe estimated radiation for these coordinates is',prediction)

        return prediction