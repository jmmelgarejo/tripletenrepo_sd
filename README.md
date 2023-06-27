## Render and Streamlit
PROJECT DESCRIPTION: 

"Fictional Scenario: We are building a platform for a purchaser who resells cars to monster truck shows and limousine dealerships. They need information on vehicle pricing, color and drivetrain in order to create a marketing plan for their inventory.

To define the client needs,

A typical vehicle for a limousine is a monochrome two-wheel drive vehicle, or a monochrome 4x4 vehicle.
A typical vehicle for a monster truck is a color 4x4 vehicle.
A third variation is a monster limo - a monochrome 4x4 vehicle.

Users on the web platform/app need to be able to 

1) Learn about pricing for vehicles
2) Filter via checkbox for more information"

FILES: 

README.md - Project information
app.py - Python file containing code for app and visual charting
EDA.ipynb - Exploratory Data Analysis of Dataset 'vehicles_us.csv'
requirements.txt - Listing of packages required for app deployment
vehicles_us.csv - Dataset used for EDA.ipynb analysis

SERVICES:
Streamlit for Visualization
Render for App Deployment

PROJECT RUBRIC/REQUIREMENTS (APP)
Created a visual with a:
    1) Scatterplot comparing odometer readings and price
    2) Checkbox option to show a histogram plot showing price for all vehicles

TO RUN LOCALLY:

You will need an interpreter such as Visual Studio Code with plugins for python and streamlit installed

1) Download listing in 'FILES' above
2) Find 'app.py' and open in interpreter such as Visual Studio Code 
3) RUN 'app.py' Note that it may be necessary to replace the rawurl with your local file path: 

rawurl = 'https://raw.githubusercontent.com/jmmelgarejo/tripletenrepo_sd/main/vehicles_us.csv'
df_vehiclesus = pd.read_csv(rawurl)

4) Once your  run the app.py code, you will need to paste the command given in terminal, with the filepath specified similar to the example below:

 streamlit run /Users/user-name/Documents/GitHub/tripletenrepo_sd/app.py

For reviewer:
6/27 - Updated README File with instructions for running the program locally
Updated model_year and odometer NaN with medians per request in EDA notebook
Note: Conclusion of the EDA findings are written in the EDA notebook under Conclusion and Recommendations.

6/20- Updated versions on requirements file.

6/19-
Render deploys the package successfully but it does not launch.
Streamlit loads locally but not on the web.  
The app could be expanded after it loads succesfully.
