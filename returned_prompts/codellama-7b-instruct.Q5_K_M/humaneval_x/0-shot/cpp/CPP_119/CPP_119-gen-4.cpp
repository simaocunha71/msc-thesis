/*
You are given an integer N and a list of N people numbered 1 to N.
Each person has a list of preferences, which are the numbers of people they
would prefer to be above them in a team.
Your job is to pair people with their preferences.
Return a vector of vectors, where the i-th element is a list of people who
are paired together.
For example:
input: 4, [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
output: [[1, 4], [2, 3], [1, 4], [2, 3]]
input: 5, [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
output: [[1, 5], [2, 4], [3, 5], [1, 4], [2, 5]]

Examples:
pair_people({4, {{1, 2, 3, 4}, {1, 2, 3, 4}, {1, 2, 3, 4}, {1, 2, 3, 4}}}) == [[1, 4], [2, 3], [1, 4], [2, 3]]
pair_people({5, {{1, 2, 3, 4, 5}, {1, 2, 3, 4, 5}, {1, 2, 3, 4, 5}, {1, 2, 3, 4, 5}, {1, 2, 3, 4, 5}}}) == [[1, 5], [2, 4], [3, 5], [1, 4], [2, 5]]
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std