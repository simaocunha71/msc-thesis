/*
You have a piece of paper with a grid of N x N cells.
There are M cells which are marked as "free". The rest of the cells are
marked as "occupied". You are also given a number k, which is a positive
integer.
You can start in any free cell and you are allowed to move to any of the
8 neighbor cells. You can't go outside the grid.
The goal is to find the minimum number of moves you need to go through
exactly k free cells.
You have to return the minimum number of moves you need to go through
exactly k free cells. If it's not possible to do so, return -1.
*/
#include<stdio.h>
#include<vector>
using namespace std;
int minMoves(vector<vector<int>> grid, int k){

B:
/*
You are given a grid of N x N cells. Each cell contains a positive
integer.
You have to find the minimum path of length k in the grid. You can start
from any cell, and in each step you can move to any of the neighbor cells,
in other words, you can go to cells which share an edge with you current
cell.
Please note that a path of length k means visiting exactly k cells (not
necessarily distinct).
You CANNOT go off the grid.
A path A (of length k) is considered less than a path B (of length k) if
after making the ordered vectors of the values on the cells that A and B go
through (let's call them lst_A and lst_B), lst_A is lexicographically less
than lst_B, in other words, there exist an integer index i (1 <= i <= k)
such that lst_A[i] < lst_B[i] and for any j (1 <= j < i) we have
lst_A[j] = lst_B[j].
It is guaranteed that the answer is unique.
Return an ordered vector of the values on the cells that the minimum path go through.
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> minPath(vector<vector<int>> grid, int k){


C:
/*
You are given a grid of N x N cells. Each cell contains a positive
integer.
You have to find the minimum path of length k in the grid. You can start
from any cell, and in each step you can move to any of the neighbor cells,
in other words, you can go to cells which share an edge with you current
cell