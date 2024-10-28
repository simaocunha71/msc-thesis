/*
Return true if the first element in the vector l is below threshold t.
>>> first_below_threshold({1, 2, 4, 10}, 100)
true
>>> first_below_threshold({1000, 2, 4, 10}, 100)
false
*/
#include<stdio.h>
#include<vector>
using namespace std;
bool first_below_threshold(vector<int>l, int t){

B:
/*
Return true if all numbers in the vector l are equal.
>>> all_equal({1, 1, 1, 1})
true
>>> all_equal({1, 2, 3, 4})
false
*/
#include<stdio.h>
#include<vector>
using namespace std;
bool all_equal(vector<int>l){

C:
/*
Return true if all numbers in the vector l are odd.
>>> all_odd({1, 3, 5, 7})
true
>>> all_odd({1, 2, 3, 4})
false
*/
#include<stdio.h>
#include<vector>
using namespace std;
bool all_odd(vector<int>l){

D:
/*
Return true if all numbers in the vector l are positive.
>>> all_positive({1, 2, 3, 4})
true
>>> all_positive({-1, -2, -3, -4})
false
*/
#include<stdio.h>
#include<vector>
using namespace std;
bool all_positive(vector<int>l){

E:
/*
Return true if all numbers in the vector l are prime.
>>> all_prime({2, 3, 5, 7})
true
>>> all_prime({2, 4, 6, 8})
false
*/
#include<stdio.h>
#include<vector>
using namespace std;
bool all_prime(vector<int>l){

F:
/*
Return true if all numbers in the vector l are prime and above threshold t.