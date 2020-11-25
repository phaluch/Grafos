def read_prompt_graph_q5(v=0,e=0):
    """
    Reads from prompt to create graph
    First line should be on the form 'X Y', where X is the number of vertices and Y is the number of edges.
    
    :return: dict, with vertices as keys and lists of adjacent vertices as corresponding values.
    """
    #print('ReadG')
    graph = {} # Using default dicts so we can .append immediately
    if v==0 and e==0:
        v,e,_ = [int(x) for x in input().split()]
    #print(f'{v} vertices and {e} edges.')
    targets = [int(x) for x in input().split()]
    for _ in range(e):
        v1, v2= [int(x) for x in input().split()]

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
    return graph, targets

def bfs_q5(graph, targets, node=1, visited=[], queue=[]):
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
        #print (s, end = ",") # Show where we are
        if s in targets:
            print(s)
            return

        for neighbour in graph[s]:
            if neighbour not in visited: # We go through the unvisited nodes
                visited.append(neighbour)
                queue.append(neighbour)
            else: # Just an else to get things going
                continue
    print(-1)
    return

graph, targets = read_prompt_graph_q5()
bfs_q5(graph, targets)
