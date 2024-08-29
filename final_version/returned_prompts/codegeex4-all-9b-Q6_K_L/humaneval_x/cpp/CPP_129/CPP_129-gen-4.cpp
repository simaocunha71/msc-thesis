/*
You are given an integer n, representing the number of cells on a side of a
square grid. Each cell is either empty or contains an integer, each integer
from 1 to n. You can move to adjacent cells, but you cannot move through
walls. You start at the top-left corner of the grid, and you must reach the
bottom-right corner of the grid, moving through as few cells as possible.
You must move up, down, left, or right, and you cannot move diagonally.
You cannot move through walls. You cannot visit the same cell more than
once.

Return the minimum number of moves required to reach the bottom-right corner
of the grid, starting at the top-left corner.

Examples:

    Input: n = 2
    Output: 2
    Explanation: The minimum number of moves required to reach the bottom-right
    corner of the grid is 2, as shown in the diagram.

    Input: n = 3
    Output: 4
    Explanation: The minimum number of moves required to reach the bottom-right
    corner of the grid is 4, as shown in the diagram.
*/
#include<stdio.h>
#include<vector>
using namespace std;
int minMoves(int n){

B:
/*
You are given a 2D grid of size n x n, where each cell contains either a
'1' or a '0'. You are also given a starting position (r0, c0) and a target
position (r1, c1). You can move from a cell (r, c) to any of the 8 adjacent
cells (r-1, c), (r+1, c), (r, c-1), (r, c+1), (r-1, c-1), (r-1, c+1), (r+1,
c-1), (r+1, c+1) if the adjacent cell contains a '1'. You cannot move to a
cell containing a '0'. You can move as many times as you want, but you cannot
move outside the grid or move to a cell that you have already visited.

Your goal is to find the minimum number of moves required to reach the target
position (r1, c1) from the starting position (r0, c0).

Examples:

    Input: grid = { {0,0,0,0,0}, {1,1,0,0,