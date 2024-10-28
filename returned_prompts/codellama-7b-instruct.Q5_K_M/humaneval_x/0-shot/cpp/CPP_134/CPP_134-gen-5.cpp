/*
Write a function called "get_unique_elements" that takes an array of integers as an argument.
The function should return an array with only the unique integers.

Examples:
get_unique_elements([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) ➞ [1, 2, 3, 4, 5]
get_unique_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
get_unique_elements([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) ➞ [1]
*/
#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;
vector <int> get_unique_elements(vector <int> arr){
    unordered_set <int> us;
    for(int i: arr)
    us.insert(i);
    return vector <int> (us.begin(), us.end());
}




