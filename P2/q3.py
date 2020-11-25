

def read_prompt_graph_q3(v=0,e=0):
    """
    Reads from prompt to create graph
    First line should be on the form 'X Y', where X is the number of vertices and Y is the number of edges.
    
    :return: dict, with vertices as keys and lists of adjacent vertices as corresponding values.
    """
    #print('ReadG')
    graph = {} # Using default dicts so we can .append immediately
    if v==0 and e==0:
        v,e = [int(x) for x in input().split()]
    #print(f'{v} vertices and {e} edges.')
    for i in range(e):
        v1, v2, P = [int(x) for x in input().split()]

        # defaultdict-functionality with list
        if v1 not in graph:
            #print("Entry for ",v1)
            graph[v1]=[]
        if v2 not in graph:
            #print("Entry for ",v2)
            graph[v2]=[]

        if v2 in graph[v1]: # Check if we already have the item
            continue
        # Fill adjacency list 'in both directions'
        graph[v1].append(v2)
        if P == 2:
            graph[v2].append(v1)
    #print('Graph returned.')
    return graph

def dfs(graph,node,visited=set()):
    """
    Prints orden of graph traversal, starting at node, using Depth-First Search.

    :param graph: Dict with nodes as keys and list of adjacent nodes as values.
    :param node: Starting node
    :param visited: Set of already visited nodes. Defaults to empty set.
    :return: None
    """
    #print(f'Começando de ---> {node}')
    #print(f'\tOs vizinhos são ---> {graph[node]}')
    #print(f'\tOs vizitados até agora são ---> {visited}')
    if node not in visited:
        visited.add(node)
        #if len(visited) == len(graph.keys()):
        #    print(node)
        #else:
        #    print(node, end=',')
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited) # recursion ftw
    #print('Visteds dentro do dfs: ',visited)
    return visited


ans = []
iterations = int(input())
for _ in range(iterations):  
    #print(f'ITERACAO {_}')  
    all_visits = set()
    graph = read_prompt_graph_q3()
    for vertex in graph.keys():
        #print(f'COMEÇANDO DO VERTEX {vertex}')
        visited = dfs(graph,vertex,set())
        all_visits.add(tuple(sorted(visited)))
#print("ALL VISITS:")
#print(f'\t {all_visits}')
    if len(all_visits) == 1:
        ans.append(1)
    else:
        ans.append(0)
    
    
for a in ans:
    print(a)