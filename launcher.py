import PySimpleGUI as sg
import networkx as nx
import math
import matplotlib.pyplot as plt
import itertools
from gui import gui_launch
from logic import G, dist, generate_graph, path_distance, best_night, optimal_drinking

if __name__ == "__main__":
    #fester är det vi får från GUI, först key är start node
    fester, max_dist = gui_launch()
    generate_graph(fester)

    #skapar möjliga vägar
    start = list(fester.keys())[0]
    valid_paths = best_night(start, max_dist, fester)

    best_path, best_alk = optimal_drinking(valid_paths)


    print(f"Festerna du ska till (i ordning från {best_path[0]} är... \n")
    print(best_path)
    print(f"Du dricker då {best_alk} enheter under nyårskvällen")