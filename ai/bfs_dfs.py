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
    visited=[node]      #array of all already visited nodes
    queue=[node]        #queue DS 
    while queue:        
        print('Visited: ',visited)
        print('Queue: ',queue)
        print('='*20)

        element=queue.pop(0)        # dequeue an element
        for n in graph[element]:
            if n not in visited:
                visited.append(n)
                queue.append(n)

    print('Visited: ',visited)
    print('Queue: ',queue)
    print('='*20)



def dfs(graph,node,visited=[]):
    if node not in visited:
        visited.append(node)
        print('Visited: ',visited)
        print('-'*10)
        for i in graph[node]:
            dfs(graph,i,visited)


print("The Depth First Search Traversal is")
dfs(graph=graph,node='5')
print()
bfs(graph=graph,node='5')

