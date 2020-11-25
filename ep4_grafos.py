"""

Pedro Terceiro Haluch Pino
1822130028
Eu documento meus códigos em inglês, não me julga.

"""

from collections import defaultdict

def read_graph(file_path, sep=';'):
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
            # print(f'Just read: {line}')
            lst = line.replace('\n','').split(sep) # Fixing some possible cosmetics problems
            for v in lst[1:]:
                if v in graph[lst[0]]: # Check if we already have the item
                    continue
                # Fill adjacency list 'in both directions'
                graph[lst[0]].append(v)
                graph[v].append(lst[0])
    return graph

def dfs(graph,node,visited=set()):
    """
    Prints orden of graph traversal, starting at node, using Depth-First Search.

    :param graph: Dict with nodes as keys and list of adjacent nodes as values.
    :param node: Starting node
    :param visited: Set of already visited nodes. Defaults to empty set.
    :return: None
    """
    if node not in visited:
        visited.add(node)
        if len(visited) == len(graph.keys()):
            print(node)
        else:
            print(node, end=',')
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited) # recursion ftw

    return visited


def fracamenteConectados(graph,visited=set()):
    """
    Prints orden of graph traversal, starting at node, using Depth-First Search.

    :param graph: Dict with nodes as keys and list of adjacent nodes as values.
    :param node: Starting node
    :param visited: Set of already visited nodes. Defaults to empty set.
    :return: None
    """
    counter = 0
    for vertex in graph.keys():
        if vertex in visited:
            continue
        else:
            counter += 1
            # print(f'\ntive que entrar por causa do {vertex}')
            visited = dfs(graph,vertex,visited)

    # print(counter)
    return counter

def dfsINOUT(graph,node,visited=set(),entrada=defaultdict(int), saida=defaultdict(int), state=0):
    """
    Prints orden of graph traversal, starting at node, using Depth-First Search.

    :param graph: Dict with nodes as keys and list of adjacent nodes as values.
    :param node: Starting node
    :param visited: Set of already visited nodes. Defaults to empty set.
    :return: None
    """
    if node not in visited:
        state+=1
        if entrada[node] == 0:
            entrada[node] = state   
        visited.add(node)
        for neighbour in graph[node]:
            visited, state, entrada, saida = dfsINOUT(graph, neighbour, visited = visited,entrada = entrada, saida=saida ,state=state) # recursion ftw
        if saida[node] == 0:
            state+=1
            saida[node] = state
    return visited, state, entrada, saida

def func():
    path = input('Nome do arquivo, no diretório atual.')
    g = read_graph(path)
    first = sorted(g.keys())[0]
    visited, state, entrada, saida = dfsINOUT(g,first)
    print(f'{"VERTICE"}\t{"IN"}\t{"OUT"}')
    for k in sorted(g.keys()):
        print(f'{k}\t{entrada[k]}\t{saida[k]}')

func()