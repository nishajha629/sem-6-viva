graph={
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
}

def bfs(graph,node):
    print("The Breadth First Search Traversal is")
    visited=[node]
    queue=[node]
    while queue:
        print('Visited: ',visited)
        print('Queue: ',queue,'\n'+'-'*20+'\n')

        t=queue.pop(0)
        for n in graph[t]:
            if n not in visited:
                visited.append(n)
                queue.append(n)
    print('Visited: ',visited)
    print('Queue: ',queue,'\n'+'-'*20+'\n')



def dfs(graph,node,visited=[]):
    if node not in visited:
        visited.append(node)
        print('Visited: ',visited)
        for i in graph[node]:
            dfs(graph,i,visited)


dfs(graph=graph,node='5')
print()
bfs(graph=graph,node='5')

