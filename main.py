import networkx as nx
mygraph = nx.read_graphml("data/code.graphml")
sorted_nodes = list(nx.topological_sort(mygraph))
print("Sorted Nodes: ", sorted_nodes)
