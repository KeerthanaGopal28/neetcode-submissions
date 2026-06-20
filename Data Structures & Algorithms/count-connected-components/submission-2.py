class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        pathMap = {i:[] for i in range(n)}
        for node1,node2 in edges:
            pathMap[node1].append(node2)
            pathMap[node2].append(node1)
        visited = set()
        count = 0
        def dfs(node,prev):
            if node in visited:
                 return
            visited.add(node)
            for i in pathMap[node]:
                if i == prev:
                    continue
                dfs(i,node)
            return True

        for i in range(n):
            if i not in visited:
                if dfs(i,i-1):
                   count+=1
        return count