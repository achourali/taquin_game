


def print_solution_path(node):
    '''
        print solution path in console
    '''
    inverted_list=[]
    while node!=None:
        inverted_list.insert(0, node)
        node=node.parent

    for node in inverted_list:
        node.taquin.display_state()



def find_node_index(node, nodes):
    for iteration, n in enumerate(nodes):
        if n.taquin.get_state() == node.taquin.get_state():
            return iteration
    return None
