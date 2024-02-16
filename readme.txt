The project has been developed for PRODIGY INFOTECH as part of my internship task-1.
It analyzes world population data using the pandas, numpy, matplotlib, and seaborn libraries. The script reads a CSV file named "world_population.csv" located in the specified directory and performs various data manipulations and visualizations.

Requirements:

Python 3.x
pandas
numpy
matplotlib
seaborn
Instructions:

Ensure that Python and the required libraries are installed on your system.
Download the "world_population.csv" file and place it in the directory specified in the script.
Execute the Python script.
Description:

Reading Data:

The script reads the "world_population.csv" file using pandas.
Data Overview:

The script displays the first few rows of the dataset using df.head().
It also shows the shape of the dataframe and information about the data types and missing values using df.shape and df.info() respectively.
Population Distribution by Continent:

It groups the data by continent and plots a pie chart showing the population distribution using matplotlib and pandas functionalities.
Top 5 Countries by Population in Each Continent:

The script creates separate dataframes for each continent.
It selects the top 5 most populated countries for each continent and plots them using seaborn's barplot.
World Population Trend:

Lastly, it visualizes the world population trend from 1970 to 2022 using a line plot.
Note:

Make sure to adjust the file path if the location of the CSV file differs.
The script assumes the structure of the CSV file remains consistent with the provided data.
Feel free to modify the script as per your requirements or for different datasets.