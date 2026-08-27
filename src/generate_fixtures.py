#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 16:53:12 2026

@author: julia
"""

import json
from max_cut import generate_graph, solve_exact

for n in [6, 9, 12]:
    graph = generate_graph(n)
    best_partition, best_cut_value = solve_exact(graph)
    
    fixture = {
        "nodes": n,
        "edges": [list(edge) for edge in graph.edges()],
        "optimal_partition": list(best_partition),
        "optimal_cut_value": best_cut_value,
        }
    
    with open(f"../fixtures/graph_{n}.json", "w") as f:
        json.dump(fixture, f, indent=2)
        
    print(f"n={n}: optimal cut = {best_cut_value}")