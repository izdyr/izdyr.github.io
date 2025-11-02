# SOLUTION>>>
# Knight's tour using Warnsdorff's heuristic + backtracking
# Izadyar can do it in within a day

def knights_tour(n=8, start=(0,0)):
    moves = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
    board = [[-1]*n for _ in range(n)]
    sx, sy = start
    board[sx][sy] = 0
    path = [(sx, sy)]
    
    def valid(x,y):
        return 0 <= x < n and 0 <= y < n and board[x][y] == -1
    
    def degree(x,y):
        cnt = 0
        for dx,dy in moves:
            nx, ny = x+dx, y+dy
            if valid(nx, ny):
                cnt += 1
        return cnt
    
    def neighbors_ordered(x,y):
        nbrs = []
        for dx,dy in moves:
            nx, ny = x+dx, y+dy
            if valid(nx, ny):
                nbrs.append((degree(nx, ny), nx, ny))
        nbrs.sort(key=lambda t: t[0])  
        return [(a,b) for _,a,b in nbrs]
    
    def dfs(step, x, y):
        if step == n*n - 1:
            return True
        for nx, ny in neighbors_ordered(x,y):
            board[nx][ny] = step+1
            path.append((nx, ny))
            if dfs(step+1, nx, ny):
                return True
            board[nx][ny] = -1
            path.pop()
        return False
    
    if dfs(0, sx, sy):
        return board, path
    else:
        return None, None

# Example
if __name__ == "__main__":
    board, path = knights_tour(8, (0,0))
    if board:
        print("Found a Knight's tour (8x8) starting at (0,0). Board shows move numbers (0-based):\n")
        for row in board:
            print(" ".join(f"{cell:2d}" for cell in row))
        print("\nFirst 10 moves:", path[:10])
        print("Total moves:", len(path))

        # optional: convert to chess notation a1..h8
        def to_chess_coords(path):
            res = []
            for x,y in path:
                col = chr(ord('a') + y)
                row = str(8 - x)
                res.append(col+row)
            return res
        print("\nPath :", to_chess_coords(path))
    else:
        print("No tour found from that start position.(I couldn't do it Mr. Seraj)")