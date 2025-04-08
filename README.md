
# A Deep Dive Into IMDb's Movie Ratings

**Ever struggled to choose the perfect Friday night movie? Same here. In this project, you'll find a summary of top-rated movies on IMDb, complete with cool visualizations — maybe it'll help you decide!**

*This repository primarily contains data, Python scripts, and plots for a project required by the course HEL-8048 25V Advanced data and visualization using programming at UiT The Arctic University of Norway.*


<img src="https://github.com/johjor/Python_Course_2025/blob/main/source/Picture_of_famous_movies.jpg" alt="IMDb Movies Dataset" width="500">

This repository is created to take a deeper look into the database of IMDb (Internet Movie Database). The database contain information related to films, television series, podcast, video games etc. At IMDb you can find information about cast, production crew, plot summaries etc. In this project I will focus on movie titles, the release year, age rating, genres, IMDb rating, number of users who rated the movies and number of user reviews for the movies.

In this project I have mainly used Pandas to manage, filter and sort the data. Different methods and functions from Matplotlib and Seaborn are used to adjust plotting and data visualization. Several visualization styles are used to plot the data. I use Jupyter Notebook in VScode to write code and markdown files, commenting my choices through the process. 

You can see the information about the repository organisation below.
*To view the final results and conclusions, see IMDb_exam.ipynb in the /results folder.*

Below you will find more information about the organization of this repository, the source of data and further details. 

---

## Table of Contents

- [Project Overview](#a-deep-dive-into-imdbs-movie-ratings)
- [The Source and Structure of Data](#the-source-and-structure-of-data)
- [Repository Organization](#repository-organization)
- [Hypothesis](#hypothesis)
- [Info Desk](#info-desk)
- [Colors Used](#colors-used)
- [License](#license)
- [Authors](#authors)

---


## The Source and Structure of Data

The data used in this project was initially downloaded from kaggle with Kagglehub API. The downloading process is further explained in the file: download_kaggle_dataset.ipynb.

**The data reflects a collection of metadata from 1500 movies from from 1936 to 2020.**

IMDb (Internet Movie Database) provides information about films, TV series, podcasts, video games, and more — including cast, crew, plot summaries, ratings, and reviews. This project focuses on:
- Movie titles
- Release year
- Age rating
- Genres
- IMDb rating
- Number of user ratings
- Number of user reviews

---

## Repository Organization

- `/data`  
  Contains the `.csv` file with the dataset.

- `/plots`  
  Stores figures generated by scripts.

- `/results`  
  Contains final results and visualizations with captions. The main notebook `IMDb_exam.ipynb` is here — check it out to see the end results.

- `/scripts`  
  Includes scripts for each hypothesis. These scripts handle filtering, grouping, and plotting. There's also a "class plotting" file where I'm experimenting with reusable plotting functions — still a work in progress! Each of the scripts is to show how the developement of the figures happened.. The final result is in the *"IMDb_exam.ipynb"* file.

- `/source`  
  Contains the image used in this `README.md`.

- `download_kaggle_dataset.ipynb`  
  Demonstrates the KaggleHub API download process.

---

## Hypothesis
H1: Movies with a higher number of reviews are more popular — and therefore, I have likely seen them.  
H2: The number of reviews is positively correlated with the number of raters.  
H3: Movies released in 2010 or later tend to receive higher ratings than older movies.  
H4: The "Action" genre has become more popular over recent decades.  
H5: Most movies in the dataset fall under the **PG-13** category, as blockbuster movies often aim for this rating to maximize audience reach.

---

## Info Desk
**How to use this repository:**

1. **Clone the repository:**  
   Open your terminal or Anaconda Prompt, navigate to your desired folder, and run:

   ```bash
   git clone https://github.com/johjor/Python_Course_2025.git


2. **Install required packages**
    Use the /source/requirements.txt file to install all dependencies. Navigate to the folder where it’s located, then run:

    ```bash
    conda install --file requirements.txt

---

## Colors Used
Yes - you are correct, I aimed for an Easter-themed repository. Why, you ask? Because the deadline of the exam is in the Easter week!!
Here are the colors used: 

#FFA23A orange
#CBD5E8 light blue
#b4caf2 
#E6F5C9 light yellow
#ACF39D light green
#00bd84 green
#a1d8ca blue green
#FFDA03 bright yellow
#F4CAE4 light pinkt
#FF88DC Persian pink
#ffc568 light orange 
#91A6FF vista blue
#9CFFFA Ice blue

---

## License
GNU GENERAL PUBLIC LICENSE
    Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>

## Use and copying
Feel free to copy or adapt parts of this project for your own learning. Please include proper credit by linking back to this repository.

If you use this project, please cite it as follows:
  **This work is based on Johanna G. Jørstad's project, available at: https://www.github.com/johjor/Python_Course_2025**

*Note* This project is not open for contributions or pull requests.

## Authors

- [@Johanna Jørstad](https://www.github.com/johjor)


