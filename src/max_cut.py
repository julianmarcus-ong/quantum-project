#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 15:53:34 2026

@author: julia
"""

import networkx as nx
# import matplotlib.pyplot as plt
import itertools

# Generate a Max-Cut graph
def generate_graph(n_nodes, seed=42):
    """Generate a random regular graph with a fixed seed for reproducibility."""
    d = 3
    if (n_nodes * d) % 2 != 0:
        d += 1
    return nx.random_regular_graph(d=d, n=n_nodes, seed=seed)

# Brute force solver

def solve_exact(graph):
    best_cut_value = 0
    best_partition = None
    n = graph.number_of_nodes()
    
    for bits in itertools.product([0, 1], repeat=n):
        cut_value = sum(
            1 for (i, j) in graph.edges() if bits[i] != bits[j]
            )
        if cut_value > best_cut_value:
            best_cut_value = cut_value
            best_partition = bits
        
    return best_partition, best_cut_value

# if __name__ == "__main__":
    # graph = generate_graph(4)
    # partition, value = solve_exact(graph)
    # print("Edges:", list(graph.edges()))
    # print("Best partition:", partition)
    # print("Best cut value:", value)

# Draw sample graphs
# graph = generate_graph(9, 42)
# nx.draw(graph)