class Solution:
    def bfs(self, adj):
        # code here
        visited = [0] * len(adj)
        queue = deque()
        
        
        result = []
        
        queue.append(0)
        
        visited[0] = 1
        
        while queue:
            node = queue.popleft()
            result.append(node)
            
            for neighbour in adj[node]:
                if not visited[neighbour]:
                    visited[neighbour] = 1
                    queue.append(neighbour)
                    
                    
        return result