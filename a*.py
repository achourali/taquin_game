from A_star_node import A_star_node
from Taquin import Taquin
import numpy as np
from copy import deepcopy
from visual_graph import *
from utilities import *

def main():

    #creating visual pdf graph
    graph = create_Digraph('solution_graphs/a_star_graph',{'shape': 'plaintext'})

    taquin = Taquin([[1," ", 3], [4, 2,6], [7,5,8]])
    # taquin=Taquin([[1,3,5],[4,2,6],[7,8," "]])
    # taquin = Taquin([[1,2,7,3], [5,6,11,4], [ 9," ",10,8]])
    # taquin = Taquin([[" ",2,7,3], [1,11,4,8], [ 5,9,6,10]])
    
    
    node = A_star_node(taquin)

    opened_nodes = []
    closed_nodes = []

    while not node.taquin.check_done():

        if find_node_index(node, closed_nodes) == None:
            closed_nodes.append(node)

            add_visual_graph_node(graph,node)

            for direction in ["up", "right", "down", "left"]:
                
                node_child = A_star_node(deepcopy(node.taquin))
                node_child.taquin.move(direction)
                node_child.parent = node
                if node_child.taquin.get_state()==node.taquin.get_state() :
                    continue
                if node.parent != None and  node_child.taquin.get_state()==node.parent.taquin.get_state():
                    continue
                node_child.set_g_cost(node.g_cost+1)
                

                if find_node_index(node_child, closed_nodes) == None:
                    opened_nodes.append(node_child)

                add_visual_graph_node(graph,node_child)
                add_visual_graph_edge(graph,node,node_child,direction)

        
        if len(opened_nodes) != 0:
            node = opened_nodes.pop(find_lower_cost_node_index(opened_nodes))
        else:
            print("no result found .")
            exit()

    print_solution_path(node)
    color_solution_nodes(graph,node)
    graph.view() 

    print("number of visited nodes = ", len(closed_nodes))



def find_lower_cost_node_index(nodes):
    lowest_cost = nodes[0].calculate_f()
    lowest_cost_node_index = 0
    for iteration, node in enumerate(nodes):
        
        node_cost = node.calculate_f()
        if node_cost <= lowest_cost:
            lowest_cost_node_index = iteration
            lowest_cost = node_cost
    return lowest_cost_node_index


if __name__ == "__main__":
    main()
