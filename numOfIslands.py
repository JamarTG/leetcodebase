class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid , i ,j):
            if i < 0 or i > len(grid)-1 or j < 0 or j > len(grid[i])-1 or grid[i][j] == '0':
                return 0 

            grid[i][j] = '0';
            dfs(grid,i+1,j)
            dfs(grid,i,j+1) 
            dfs(grid,i-1,j)
            dfs(grid,i,j-1) 

            return 1 
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    count += dfs(grid , i , j)
        return count