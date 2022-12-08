import ast

with open('D:\\graph.txt') as f :
    data=f.read( )
graph = ast.literal_eval( data )
visited = set()  # Set to keep track of visited nodes of graph.

def dfs(v, graphh, node):  # function for dfs if node not in visited:
    print(node)
    v.add(node)
    for neighbour in graphh[node]:
        dfs(v, graphh, neighbour)


print("Following is the Depth-First Search")
dfs(visited, graph, '5')
