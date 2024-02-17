Excited to share that I've successfully completed my first task as a Data Science Intern at Prodigy Infotech! 📊 

**TASK_01**: Create a bar chart or histogram to visualize the distribution of a categorical or continuous variable, such as the distribution of ages or genders in a population.

During this experience, I had the opportunity to analyze and interpret data about the bar chart and histogram, it is a graphical representation of the distribution of data points in a dataset. 

🔍 I applied my skills with the help of VSCode notebook to uncover insights, enhance decision-making processes, and analyze the pattern of the dataset. 📈

🔍 Actively engaged in continuous learning, staying abreast of the latest trends in data science and technology. 🚀 Excited about the opportunity to apply my expanding skill set to future projects and challenges.

🌐 Grateful to be part of a forward-thinking organization like Prodigy Infotech, where innovation and creativity are valued. Looking forward to further contributing to the company's success and my own development in the world of data science. 🤝 Grateful for the support at Prodigy Infotech. Looking forward to continuing to learn and grow in the dynamic field of data science! 💼

## Requirements

- Python 3.11.7 or any Python 3 version
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`

## Instructions

1. Ensure that Python and the required libraries are installed on your system.
2. Download the "world_population.csv" file and place it in the directory specified in the script.
3. Execute the Python script.

## Description

### Reading Data

- The script reads the "world_population.csv" file using `pandas`.

### Data Overview

- The script displays the first few rows of the dataset using `df.head()`.
- It also shows the shape of the dataframe and information about the data types and missing values using `df.shape` and `df.info()` respectively.

### Population Distribution by Continent

- It groups the data by continent and plots a pie chart showing the population distribution using `matplotlib` and `pandas` functionalities.

### Top 5 Countries by Population in Each Continent

- The script creates separate dataframes for each continent.
- It selects the top 5 most populated countries for each continent and plots them using `seaborn`'s `barplot`.

### World Population Trend

- Lastly, it visualizes the world population trend from 1970 to 2022 using a line plot.

## Note

- Make sure to adjust the file path if the location of the CSV file differs.
- The script assumes the structure of the CSV file remains consistent with the provided data.
- Feel free to modify the script as per your requirements or for different datasets.
