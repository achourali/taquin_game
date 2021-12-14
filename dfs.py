from Node import Node
from Taquin import Taquin
import sys
from copy import deepcopy
import numpy as np
from visual_graph import *
from utilities import *

''' Depth First Search '''
def dfs(initial_state):


    graph = create_Digraph('solution_graphs/dfs_graph',{'shape': 'plaintext'})
    

    node=Node(Taquin(initial_state))

    opened_nodes = []
    closed_nodes = []


    while not node.taquin.check_done():
        print(len(closed_nodes))
        if find_node_index(node, closed_nodes)== None:
            closed_nodes.append(node)

            add_visual_graph_node(graph,node)
            
            
            for direction in ["up", "right", "down", "left"]:
                node_child=Node(deepcopy(node.taquin))
                node_child.taquin.move(direction)
                node_child.parent=node
                if node_child.taquin.get_state()==node.taquin.get_state() :
                    continue
                if node.parent != None and  node_child.taquin.get_state()==node.parent.taquin.get_state():
                    continue
                if find_node_index(node_child, closed_nodes)== None:
                    opened_nodes.insert(0,node_child)
                
                add_visual_graph_node(graph,node_child)
                add_visual_graph_edge(graph,node,node_child,direction)
            

        if len(opened_nodes) != 0:
            node = opened_nodes.pop(0)
        else:
            print("no result found .")
            exit()


    if(node.taquin.check_done()):
        print_solution_path(node)
        color_solution_nodes(graph,node)
        graph.view() 
        print("solved :) .")

    
    print("number of visited nodes = ", len(closed_nodes))




