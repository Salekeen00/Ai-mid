from collections import deque

def bfs(adj_matrix, start):
    
    num_vertices = len(adj_matrix)
    
    
    visited = [False] * num_vertices
    
   
    queue = deque()
    
    
    queue.append(start)
    visited[start] = True
    
    while queue:
       
        current_vertex = queue.popleft()
        print(f"Visited: {current_vertex}")
        
        
        for neighbor in range(num_vertices):
            if adj_matrix[current_vertex][neighbor] == 1 and not visited[neighbor]:
               
                queue.append(neighbor)
                visited[neighbor] = True


adjacency_matrix = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0]
]

start_vertex = 0
bfs(adjacency_matrix, start_vertex)
