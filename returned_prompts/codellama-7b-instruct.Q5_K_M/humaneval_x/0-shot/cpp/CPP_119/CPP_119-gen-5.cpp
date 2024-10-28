/*
You are given a list of integers. Your job is to return a list of
all the pairs of integers in the list that add up to 10.

Examples:
ten_pair({1, 2, 3, 4, 5, 6, 7, 8, 9}) == {{1, 9}, {2, 8}, {3, 7}, {4, 6}}
ten_pair({1, 2, 3, 4, 5, 6, 7}) == {{1, 9}, {2, 8}, {3, 7}, {4, 6}}
ten_pair({1, 2, 3, 4, 5, 6}) == {{1, 9}, {2, 8}, {3, 7}, {4, 6}}
ten_pair({1, 2, 3, 4, 5}) == {{1, 9}, {2, 8}, {3, 7}, {4, 6}}
ten_pair({1, 2, 3, 4}) == {{1, 9}, {2, 8}, {3, 7}, {4, 6}}
ten_pair({1, 2}) == {{1, 2}, {2, 1}}
ten_pair({1}) == {{1, 1}}
ten_pair({}) == {}
*/
#include<stdio.h>
#include<vector>
using namespace std;
