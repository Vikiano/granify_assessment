# granify_assessment

## part 1
Energy Consumption Forecasting
This project aims to predict the energy consumption for a day in the future using a dataset of energy consumed every hour for the years 2010 - 2018. The final submission includes the Python code and the Jupyter notebooks used, observations, approach, and conclusion..

Data
The data used in this project is energy consumed in MWH for years 2010 - 2018. The data contains the following columns: Datetime (yyyy-mm-dd-hh), Power_MWH
The data can be found at the following location:
https://drive.google.com/file/d/1NCl2EEvGzUfDId5drk1nY6O6ecR5XEaq/view?usp=sharing

### Data Analysis
- Visualization and statistical exploration of data to understand the nature of data.
- Check for stationarity using the Augmented Dickey-Fuller test.
- Check for outliers.
- Test for seasonality using the STL decomposition method.

### Feature Engineering
- Extracted new features from the data that will help achieve the end goal.
- New features are: hour	dayofweek	month	year	lag_1h	lag_24h	rolling_mean_24h	rolling_std_24h

### Baseline Model
Here, a mean model was compared to a median model. Since the median model has the lower Mean Squared Error, the median model is the best baseline here.

### Machine Learning Models
- Here, XGBRegressor and SVR were used. XGBoost is the best Machine Learning Model here since it has the least mean squared error in this case.y.

Python 3.6 or higher
pandas
numpy
matplotlib
statsmodels
sklearn
xgboost

### Running the Code
Clone the repository:
Copy code
git clone https://github.com/Vikiano/granify_assessment.git

## part 2

This project is an example of an object-oriented program that simulates a pet shop. It includes classes for cats and dogs and a fake database connection.

### Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
Python 3.x
unittest library
A text editor
SQL (for the SQL Tasks)

### Installing
Clone the repository to your local machine

git clone https://github.com/Vikiano/granify_assessment-shop-project.git
Navigate to the project directory

cd pet-shop-project
Run the main script to see the initial functionality

python main.py
Run the test script to ensure that the classes are working correctly

python test_cat.py
Running the tests
To run the tests for the Cat class, you can use the following command

python test_cat.py
To run the tests for the Dog class, you can use the following command


python test_dog.py
Built With
Python - The programming language used
unittest - The unit testing framework for Python