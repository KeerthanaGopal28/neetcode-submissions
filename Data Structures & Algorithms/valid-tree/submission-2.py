class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True
        visited = set()
        pathMap = {i:[] for i in range(n)}
        for node,nextNode in edges:
            pathMap[node].append(nextNode)
            pathMap[nextNode].append(node)    
        def dfs(node,prev):
            if node in visited:
                return False
            visited.add(node)
            for i in pathMap[node]:
                if i == prev:
                    continue
                if not dfs(i,node):
                    return False
            return True
        return dfs(0,-1) and len(visited) == n

