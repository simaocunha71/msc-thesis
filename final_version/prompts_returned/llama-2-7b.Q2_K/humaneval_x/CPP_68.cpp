/*
Given a vector representing a branch of a tree that has non-negative integer nodes
your task is to pluck one of the nodes and return it.
The plucked node should be the node with the smallest even value.
If multiple nodes with the same smallest even value are found return the node that has smallest index.

The plucked node should be returned in a vector, { smalest_value, its index },
If there are no even values or the given vector is empty, return {}.

Example 1:
    Input: {4,2,3}
    Output: {2, 1}
    Explanation: 2 has the smallest even value, and 2 has the smallest index.

Example 2:
    Input: {1,2,3}
    Output: {2, 1}
    Explanation: 2 has the smallest even value, and 2 has the smallest index. 

Example 3:
    Input: {}
    Output: {}

Example 4:
    Input: {5, 0, 3, 0, 4, 2}
    Output: {0, 1}
    Explanation: 0 is the smallest value, but  there are two zeros,
                 so we will choose the first zero, which has the smallest index.

Constraints:
    * 1 <= nodes.length <= 10000
    * 0 <= node.value
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> pluck(vector<int> arr){
     vector<int> ans;
     for (size_t i = arr.size() - 1; i >=0 ; --i) {//start from last index to 0th index
         if((arr[i] %2 == 0) && ((arr[0] %2 !=0))){//check is the even number or not
             ans.push_back(arr[i]); // if its odd than we will return null
             break;
         } else if (ans.size() > 0){
             continue;
         }else {//if not odd then push back in vector with index
             ans.push_back((int) i