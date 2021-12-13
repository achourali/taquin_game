import graphviz

# functions used in creating visual pdf graph


def create_Digraph(path,node_attr):
    return graphviz.Digraph(path, filename=path+'.gv', node_attr=node_attr)

def add_visual_graph_node(graph,node):
    graph.node(node.generate_id(),node.generate_html_table())
def add_visual_graph_edge(graph,node1,node2,label):
    graph.edge(node1.generate_id(),node2.generate_id(),label)

def color_solution_nodes(graph,solution_node):
    node=solution_node
    while node!=None:
        graph.node(node.generate_id(),style='filled', fillcolor='#40e0d0')
        node=node.parent
