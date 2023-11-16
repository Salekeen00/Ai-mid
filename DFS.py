from collections import deque
def dfs(adj_matrix, start, visited):
    
    print(f"Visited: {start}")
    
    
    visited[start] = True
    
   
    for neighbor in range(len(adj_matrix)):
        if adj_matrix[start][neighbor] == 1 and not visited[neighbor]:
            
            dfs(adj_matrix, neighbor, visited)

def dfs_main(adj_matrix, start):
    
    num_vertices = len(adj_matrix)
    
    
    visited = [False] * num_vertices
    
   
    dfs(adj_matrix, start, visited)


adjacency_matrix = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0]
]

start_vertex = 0
dfs_main(adjacency_matrix, start_vertex)
