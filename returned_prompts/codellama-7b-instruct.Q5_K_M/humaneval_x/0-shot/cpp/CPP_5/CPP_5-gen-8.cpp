/*
Find the largest number in the vector `numbers`
>>> max({1, 2, 3})
3
>>> max({3, 2, 1})
3
*/
#include<stdio.h>
#include<vector>
using namespace std;
int max(vector<int> numbers){ 

B:
/*
Find the number of elements in vector `numbers`
>>> size({1, 2, 3})
3
*/
#include<stdio.h>
#include<vector>
using namespace std;
int size(vector<int> numbers){ 

C:
/*
Concatenate `numbers` and `numbers` itself
>>> concat({1, 2, 3}, {1, 2, 3})
{1, 2, 3, 1, 2, 3}
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> concat(vector<int> numbers, vector<int> numbers2){ 

D:
/*
Remove the first element of vector `numbers`
>>> tail({1, 2, 3})
{2, 3}
>>> tail({})
{}
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> tail(vector<int> numbers){ 

E:
/*
Reverse the vector `numbers`
>>> reverse({1, 2, 3})
{3, 2, 1}
>>> reverse({})
{}
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> reverse(vector<int> numbers){ 

F:
/*
Find the first occurrence of number `target` in vector `numbers`
>>> find({1, 2, 3, 4, 5}, 3)
2
>>> find({1, 2, 3, 4, 5}, 6)
-1
*/
#include<stdio.h>
#include<vector>
using namespace std;
int find(vector<int> numbers, int target){ 

G:
/*