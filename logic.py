from networkx.algorithms import approximation as approx

import networkx as nx
import math
import matplotlib.pyplot as plt
import itertools

global G
G = nx.Graph()

def dist(p0, p1):
    dist = math.sqrt( sum( [abs(i-j)**2 for i, j in zip(p0,p1) ] ) )

    return int(round(dist, 0))

def generate_graph(fester = False):
    edges = {i:{} for i in fester.keys()}

    for fest in fester.keys():
        p0 = fester[fest]["pos"]

        for key in set(fester.keys()) - set({fest}):
            p1 = fester[key]["pos"]
            distance = dist(p0, p1)
            edges[fest][key] = distance

    every_edge = []
    for key, val in edges.items():
        for destination, weight in val.items():
            every_edge.append( (key, destination, weight) )

    for FEST in fester.keys():
        G.add_node(FEST, alkohol = fester[FEST]["alkohol"], party = True)
    G.add_weighted_edges_from(every_edge)


def path_distance(path):
        weight = 0
        for i in range(len(path)-1):
            weight += (G[path[i]][path[i+1]]["weight"])
        return weight

def best_night(start, max_length, fester):
    possi = set(fester.keys()-{start})
    alk_max = 0
    valid_paths = []


    for each in possi:
        for path in nx.all_simple_paths(G, source=start, target=each):
            
            length_travelled = path_distance(path)

            #length_travelled = nx.path_weight(G, path, weight="weight")

            if length_travelled < max_length:

                valid_paths.append([path, length_travelled])

    return valid_paths

def path_distance(path):
        weight = 0
        for i in range(len(path)-1):
            weight += (G[path[i]][path[i+1]]["weight"])
        return weight


def optimal_drinking(valid_paths):
    results = []
    for path in valid_paths:
        #a valid path never revisits a node
        dricka = 0

        #count the drinks from the path
        for place in path[0]:
            dricka += G.nodes[place]["alkohol"]
        results.append( [path[0], dricka, path[1] ])

    best_alk = 0
    best_path = []

    for route in results:
        if route[1] > best_alk:
            best_alk = route[1]
            best_path = route[0]

    return best_path, best_alk

