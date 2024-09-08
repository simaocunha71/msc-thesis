/*
Return the sum of numbers in the vector l.
>>> sum_numbers({1, 2, 4, 10})
17
>>> sum_numbers({1, 20, 4, 10})
35
*/
#include<stdio.h>
#include<vector>
using namespace std;
int sum_numbers(vector<int>l){

B:
/*
Return the number of elements in the vector l.
>>> count_elements({1, 2, 4, 10})
4
>>> count_elements({1, 20, 4, 10})
4
*/
#include<stdio.h>
#include<vector>
using namespace std;
int count_elements(vector<int>l){

C:
/*
Return the number of elements in the vector l that are above threshold t.
>>> count_above_threshold({1, 2, 4, 10}, 5)
1
>>> count_above_threshold({1, 20, 4, 10}, 5)
2
*/
#include<stdio.h>
#include<vector>
using namespace std;
int count_above_threshold(vector<int>l, int t){

D:
/*
Return the sum of numbers in the vector l that are above threshold t.
>>> sum_above_threshold({1, 2, 4, 10}, 5)
6
>>> sum_above_threshold({1, 20, 4, 10}, 5)
24
*/
#include<stdio.h>
#include<vector>
using namespace std;
int sum_above_threshold(vector<int>l, int t){

E:
/*
Return a new vector that contains all numbers in the vector l that are above threshold t.
>>> filter_above_threshold({1, 2, 4, 10}, 5)
{6}
>>> filter_above_threshold({1, 20, 4, 10}, 5)
{20, 10}
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int>filter_above_threshold(vector<int>l, int t){

F:
/*
Return a new vector that contains all numbers in the vector l that are below threshold t.
>>> filter_below_threshold({1, 2, 4, 10}, 5)
{1, 2, 4}
>>> filter_below_threshold({1, 20, 4, 10}, 5)
{1, 4}
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int>filter_below_threshold(vector<int>l, int t){

G:
/*
Return a new vector that contains all numbers in the vector l that are below