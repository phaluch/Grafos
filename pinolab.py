"""

Pedro Terceiro Haluch Pino
1822130028
Eu documento meus códigos em inglês, não me julga.

"""

import argparse
from collections import defaultdict

# So the user can input the filepath directly from the command line
parser = argparse.ArgumentParser(description='Devolve Matriz e Lista de Adjacência.')
parser.add_argument('arquivo', metavar='f', type=str, nargs='?', default=False, help='Nome do arquivo .csv')

# Bringing it to the local namespace
args = parser.parse_args()
file_path = args.arquivo

# If user hasn't input the file name, asks for it
if not file_path:
    file_path = input('Nome do arquivo por favorzinho.\n')

# Making sure the .csv is actually a .csv
assert file_path.endswith('.csv'), 'Tem que ser .csv filho.'


def read_graph(file_path, sep=','):
    """
    Created a graph as a dict from a .csv or .txt file.

    :param file_path: Complete or relative file path.
    The file can contain any number of lines, with vertices' labels separated by commas.
    The first label will be considered to current vertex, and all subsequent labels in the same line will be
    considered adjacent to the current vertex.
    :param sep: separator being used in the .csv file. Defaults to the comma character.

    :return: dict, with vertices as keys and lists of adjacent vertices as corresponding values.
    """
    with open(file_path) as f:
        graph = defaultdict(list) # Using default dicts so we can .append immediately
        for line in f.readlines():
            print(f'Just read: {line}')
            lst = line.replace('\n','').split(sep) # Fixing some possible cosmetics problems
            for v in lst[1:]:
                if v in graph[lst[0]]: # Check if we already have the item
                    continue
                # Fill adjacency list 'in both directions'
                graph[lst[0]].append(v)
                graph[v].append(lst[0])
    return graph


visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(graph, node, visited=[], queue=[]):
    """
    Breadth-first approach: Going level by level in a graph until all nodes have been visited.

    :param visited: List of nodes by which we've already gone
    :param queue: Ordered sequence of next nodes to be visited
    :param graph: dict with strings as keys, and lists of strings as values
    :param node: Starting node for the BFS algorithm
    :return: string of the visited nodes, in reading order
    """

    # Adding the source node in both lists so it isn't counted twice
    visited.append(node)
    queue.append(node)

    while queue: # We iterate until the queue is empty
        s = queue.pop(0) # Get the first element in the queue
        print (s, end = ",") # Show where we are

        for neighbour in graph[s]:
            if neighbour not in visited: # We go through the unvisited nodes
                visited.append(neighbour)
                queue.append(neighbour)
            else: # Just an else to get things going
                continue
    print('')

def dfs(graph,node,visited=set()):
    """
    Prints orden of graph traversal, starting at node, using Depth-First Search.

    :param graph: Dict with nodes as keys and list of adjacent nodes as values.
    :param node: Starting node
    :param visited: Set of already visited nodes. Defaults to empty set.
    :return: None
    """

    if node not in visited:
        print(node, end=',')
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited) # recursion ftw

# Reading the csv file into a graph
graph = read_graph(file_path,';')
print(graph)
# And picking the starter value
start_point = sorted(list(graph.keys()))[0]

print('Lista de Adjacência')
for k in graph.keys():
    print(f'{k}:{graph[k]}')
print(f'Ordem percorrida, saindo do vértice {start_point}:')
dfs(graph,start_point)