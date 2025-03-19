
# A Deep Dive Into IMDb's Movie Ratings

**This repository primarily contains data, Python scripts, and plots for a project required by the course HEL-8048 25V Advanced data and visualization using programming at UiT The Arctic University of Norway.**

![IMDB Movies Dataset](https://github.com/johjor/Python_Course_2025/blob/main/Picture_of_famous_movies.jpg)

Below you will find more information about the organization of this repository, the source of data and further details. 

In this project I have mainly used Pandas to manage, filter and sort the data. Different methods and functions from Matplotlib are used to adjust plotting and data visualization. The notebook hel8048_project.ipynb contains the process of grouping data and making plots (i.e not just the end result). Several visualization styles are used to plot the data.


# The source and structure of data

The data used in this project was initially downloaded from kaggle. The downloading process is further explained in the file: download_kaggle_dataset.ipynb.

**The data reflects a collection of metadata from 1050 movies from from 1936 to 2020.**

# The organization of this repository
* /data stores .csv files containing data used in this project
* /notebooks is where you will find the script used in this project to filter, group and plot the data, the only script you need to use is hel8048_project.ipynb
* /plots is the folder where the figures generated by the script are stored
* /results is the folder where the "final" results and plots of the study are represented with captions, this directory also contains a separate "readme" file that will be automatically displayed as soon as you open the link.

# Hypothesis
H1: The movie genre "Action" have become more popular over the decades. To investigate this I plan to use a line chart to show the numbers released in each genre over time.

H2: Movies relased during autumn tend to have higher user ratings. To investigate this I will use a heatmap or bar chart to show average user ratings by release month.

H3: Movies that have won major awards (e.g. Oscars) have higher user ratings. To investigate this I want to compare the avarage user ratings of award-winning movies to those that haven't won awards using a bar chart. 

H4: Movies directed by ceratin directors (e.g. Tarantino, Nolen) consistently receive higher user ratings. I will visualize this by using a scatter plot or bar chart to compare average user ratings for movies by different directors. 

H5: Higher-budget movies tend to receive higher user ratings. I will use a scatterplot to show the relationship between movie budget and user ratings. 

# Info desk
**How to use this repository?**

* Clone the repository: run your anaconda prompt (terminal), change directory to your desired pathway and use this command:
          git clone https://github.com/johjor/Python_Course_2025.git

* In case you are missing some packages used in this project, you can use the "/source/requirements.txt" to install them all at once. In order to install the packages, you can use the command below either in your base environment or any other specific environment:
         conda install --file requirements.txt
before running the command, make sure to change the directory to the pathway where the files is stored.


## Authors

- [@Johanna Jørstad](https://www.github.com/johjor)

