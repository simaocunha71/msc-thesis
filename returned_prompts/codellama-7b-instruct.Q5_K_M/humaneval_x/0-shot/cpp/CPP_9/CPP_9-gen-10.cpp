/*
Given two sorted vector of integers, merge them into a single sorted vector
>>> merge({1, 3, 5}, {2, 4, 6})
{1, 2, 3, 4, 5, 6}
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> merge(vector<int> a, vector<int> b){

B:
/*
Given two vectors of integers, return a vector of unique elements that appear
in either of the two input vectors.
>>> intersect({1, 2, 3}, {4, 5, 6})
{1, 2, 3, 4, 5, 6}
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> intersect(vector<int> a, vector<int> b){

C:
/*
Given a vector of integers, return a new vector of the same size, containing
the element at the current index plus the size of the original vector minus
the current index.
>>> reverse({1, 2, 3})
{3, 2, 1}
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> reverse(vector<int> a){

D:
/*
Given a vector of integers, return a vector of the same size, containing the
sum of all elements up to the current index, but not including the current
index'th element.
>>> prefix_sum({1, 2, 3})
{1, 3, 6}
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> prefix_sum(vector<int> a){

E:
/*
Given a vector of integers, return the index of the first element equal
to the given target. If there is no such element, return -1.
>>> find({1, 2, 3, 4, 5}, 3)
2
*/
#include<stdio.h>
#include<vector>
using namespace std;
int find(vector<int> a,