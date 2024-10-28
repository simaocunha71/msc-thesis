/*
Write a function that accepts a list of integers and a target integer.
The function should return a new list containing the elements from the
original list that sum to the target.
The function should not modify the original list.
For example:
assert list_sum( [1,2,3,4,5,6,7,8,9], 15 ) => [1,2,3,4,9]
assert list_sum( [1,2,3,4,5,6,7,8,9], 10 ) => [1,2,3,4,5,6,7,8,9]
assert list_sum( [1,2,3,4,5,6,7,8,9], 100 ) => []
*/
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> list_sum(vector<int> lst, int target){

B:
/*
Write a function that accepts a vector of integers and a target integer.
The function should return a new vector containing the elements from the
original vector that sum to the target.
The function should not modify the original vector.
For example:
assert vector_sum( [1,2,3,4,5,6,7,8,9], 15 ) => [1,2,3,4,9]
assert vector_sum( [1,2,3,4,5,6,7,8,9], 10 ) => [1,2,3,4,5,6,7,8,9]
assert vector_sum( [1,2,3,4,5,6,7,8,9], 100 ) => []
*/
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> vector_sum(vector<int> vec, int target){

C:
/*
Write a function that accepts a vector of strings and returns a vector of
strings in a sorted order based on the length of each string.
For example:
assert sorted_vector({"aa", "a", "aaa"}) => {"a", "aa", "aaa"}
assert