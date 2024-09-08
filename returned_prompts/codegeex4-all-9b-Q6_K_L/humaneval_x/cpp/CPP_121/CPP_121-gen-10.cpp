/*
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> solutions(vector<int> lst){

B:
/*
You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return an empty array.

Example

sortArray([5, 3, 2, 8, 1, 4]) ==> [1, 3, 2, 8, 5, 4]

sortArray([5, 3, 1, 8, 0]) ==> [1, 3, 5, 8, 0]

Starter code:

```
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> solutions(vector<int> lst){
```