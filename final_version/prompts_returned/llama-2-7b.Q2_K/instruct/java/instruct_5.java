Write a method in a graph database that adds a random number of vertices and edges to the graph, and sets random properties on the vertices and edges, using the standard library functions.

    Only return the code, don't include any other information,
    such as a preamble or suffix.
"""
from random import randint
import pydotplus
import cPickle as pickle
import os
import sys

sys.path.append('D:\dev\pydot-graph')

def get_rand_num(max):
    return randint(-1, max)

def set_vertex_random():
    return {'random': get_rand_num(5)}

def add_random_edge():
    return {'edges': [('a', 'b')]}
    


def main():
    graph = pydotplus.AGraph()
    with open("graph.pickle") as f:
        code, vertices, edges = pickle.load(f)
    graph.add_node_attributes(vertices)
    graph.add_edge_attributes(edges)
    
    for i in range(10):
        random_vertex = get_rand_num()
        
        if random_vertex < 3:
            code += add_random_edge() + '\n'
        
        if random_vertex > 2 and random_vertex < 5:
            for j in range(1, min(3 - random_vertex, 3)):
                set_vertex_random(), code

if __name__ == '__main__':
    main()