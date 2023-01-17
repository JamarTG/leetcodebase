def dfs(grid , i ,j):
        if i < 0 or i > len(grid) or j < 0 or j > len(grid[i]) or grid[i][j] == '0':
            return 

        dfs(grid[i+1][j])
        dfs(grid[i][j+1]) 
        dfs(grid[i-1][j])
        dfs(grid[i][j-1]) 

        return 1 