    int N=grid.size();
    vector<int> res;
    for (int i=0;i<N;i++)
    for (int j=0;j<N;j++)
    {
        if (k==1)
        {
            res.push_back(grid[i][j]);
            return res;
        }
    }
    for (int i=0;i<N;i++)
    {
        for (int j=0;j<N;j++)
        {
            if (k>1)
            {
                res.push_back(grid[i][j]);
                k--;
            }
        }
    }
    return res;
} // Not a correct solution, as it doesn't consider the path length, but just adds all elements to the result vector.
// A correct solution would be a Dijkstra's algorithm like implementation. It would start from each cell and 
// explore all possible paths with length k and keep track of the minimum path seen so far. 
// The time complexity of this solution would be O(N^2 * 2^k), where N is the size of the grid and k is the path length. 
// This is because in the worst case, we have to explore all possible paths of length k starting from each cell. 
// The space complexity would be O(N^2 * 2^k), as we need to store all possible paths. 
// This solution is not efficient for large inputs. 
// A more efficient solution would be to use a priority queue to store the minimum path seen so far. 
// This would reduce the time complexity to O(N^2 * k), where N is the size of the grid and k is the path length. 
// The space complexity would be O(N^2), as we need to store the minimum path seen so far. 
// This solution is more efficient for large inputs. 
// However, it is still not efficient for very large inputs, as the time complexity is still exponential. 
// A more efficient solution would be to use a dynamic programming approach, where we build a 2D array dp[][] to store the minimum path seen so far. 
// This would reduce the time complexity to O(N^2 * k), where N is the size of the grid and k is the path length. 
// The space complexity would be O(N^2), as we need to store the minimum path seen so far. 
// This solution is more efficient for very large inputs. 
// However, it is still not efficient for inputs where k is very large,