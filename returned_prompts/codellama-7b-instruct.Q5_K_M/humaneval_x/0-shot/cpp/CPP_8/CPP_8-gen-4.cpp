/*
Given a number n, create a vector of length n filled with the numbers from 1 to n.
If n < 0, return an empty vector.
If n == 0, return a vector containing only 0.
>>> create_vector(0)
[0]
>>> create_vector(5)
[1, 2, 3, 4, 5]
>>> create_vector(-1)
[]
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> create_vector(int n){

B:
/*
For a given vector of integers, return a vector containing only the first and last elements of the original vector.
If the original vector has less than two elements, return an empty vector.
>>> first_last({1, 2, 3, 4, 5})
[1, 5]
>>> first_last({1})
[1]
>>> first_last({})
[]
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> first_last(vector<int> numbers){

C:
/*
Given a vector of integers, return a vector containing the elements from the second last element to the last element of the original vector.
If the original vector has less than two elements, return an empty vector.
>>> second_last_to_last({1, 2, 3, 4, 5})
[3, 4, 5]
>>> second_last_to_last({1, 2, 3})
[2, 3]
>>> second_last_to_last({1})
[]
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> second_last_to_last(vector<int> numbers){

D:
/*
Given a vector of integers, return a vector containing all the even numbers of the original vector.
If there are no even numbers in the original vector, return an empty vector.
>>> only_even({2, 4, 6, 8, 10})
[2, 4, 6, 8, 1