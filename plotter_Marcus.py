import matplotlib.pyplot as plt
import csv
import pandas as pd

class Plotter():
    def __init__(self, data_path):
        self.csv_path = data_path
                
        # key = plot, value = plotting function
        self.plot_dict = {
            0:self.action_by_year,
            1:self.movies_per_season
        }
    
    def determine_plot(self, plot):
        # call function based on the plot you want
        self.plot_dict[plot]()

    # plotting function 1
    def action_by_year(self):
        print("Action by year")
        # save the plot to plots folder
    
    # plotting function 2
    def movies_per_season(self):
        print("Movies per season")
        # save the plot to plots folder
        
if __name__ == "__main__":
    movie_data_plotter = Plotter("../data/test.csv")
    
    num_plots = 10
    
    for i in range(num_plots):
        movie_data_plotter.determine_plot(i)