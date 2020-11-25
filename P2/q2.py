"""
Pedro Terceiro Haluch Pino
1822130028
P2 - Q2
"""

def read_prompt_graph(v=0,e=0):
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
        v1, v2 = [int(x) for x in input().split()]

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
        graph[v2].append(v1)
    #print('Graph returned.')
    return graph


def distanceFromRootBFS(graph, root):
    """
    Retorna dicionário com distâncias dos vértices de graph, em saltos, de root.
    """
    visited = []
    d = 0
    distances = {root:d}
    q = [root]
 
    while q:
        node = q.pop(0)
        #print(f'Visitando nó {node}.')
        #print(f'Distancia atual: {distances[node]}')
        d=distances[node]+1
        #print(f'Proximas distnacias: {d}')
        #print(f'DDDD: {distances}')
        if node not in visited:
            #print('    Não foi visitado antes: q')
            visited.append(node)
            neighbours = graph[node]
 
            
            for neighbour in neighbours:
                #print(f'Vizinhos são {neighbours}')
                if neighbour not in distances:
                    #print(f'{neighbour} ainda não tem distancia --> {d}.')
                    distances[neighbour] = d
                q.append(neighbour)
    return distances


C,E,L,P = [int(x) for x in input().split()]
graph = read_prompt_graph(C,E)

distances = distanceFromRootBFS(graph,L)

ans = [e for e,d in distances.items() if d <= P and e != L]
print(' '.join([str(n) for n in sorted(ans)]))