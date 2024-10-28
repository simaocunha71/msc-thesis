    vector<string> new_list;

B:
    for(int i=0; i < lst.size(); i++){
        if(lst[i].length() % 2 == 0){
            new_list.push_back(lst[i]);
        }
    }

C:
    sort(new_list.begin(), new_list.end());

D:
    return new_list;
}

int main() {
    vector<string> vec = {"ab", "a", "aaa", "cd"};
    vector<string> res = sorted_list_sum(vec);
    for(int i = 0; i< res.size(); i++){
        printf("%s ", res[i].c_str());
    }
    return 0;
}


A: Initializing a new list of strings, new_list, to store the strings with even lengths.

B:
Iterating over each string in the input list, lst. If the length of the string is even (i.e., the modulus of the string length by 2 is 0), it is added to new_list.

C:
Sorting the new_list using the sort function.

D:
Returning the sorted list, new_list.

The main function tests the sorted_list_sum function by passing a vector of strings, and it prints the returned vector.
*/

//Q2:
/*
Write a function named "max_min" that accepts an integer vector and returns a pair of integers.
The pair consists of the maximum and the minimum values in the vector.
If the vector is empty, the function should return a pair of 0, 0.

For example:
assert max_min({1, 2, 3, 4, 5}) => (5, 1)
assert max_min({-1, -2, -3, -4, -5}) => (-1, -5)
assert max_min({}) => (0, 0)

*/

#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;

pair<int, int> max_min(vector<