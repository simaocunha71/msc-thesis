/*
Create a function that returns a vector (a, b), where "a" is
the largest of negative integers, and "b" is the smallest
of positive integers in a vector.
If there is no negative or positive integers, return them as 0.

Examples:
largest_smallest_integers({2, 4, 1, 3, 5, 7}) == {0, 1}
largest_smallest_integers({}) == {0,0}
largest_smallest_integers({0}) == {0,0}
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> largest_smallest_integers(vector<int> lst){
	if(lst.size()==0) return {0}; // if zero size, return 0
	
	// If there's only negative integers in the list:
	if(lst[0] < 0 && !(lst.size() == 1 || (lst[0]+9)>=-1 && lst[0]>-1)) { // if all negative numbers,
	    return {-1};                      // return -1 because none positive
	} else if(lst[0] < 0) {              // Else, return 0 and the first positive number
	    return ({0, lst.at(0)})        // in the list;
	} else {                // End of conditionals:
	    for (int i = 1; i < lst.size(); i++) {      // If there are more than one numbers,
	    	if ((lst[i] >-1 &&!0) || (lst[i] == 9+i && !0)) {}                        // and first positive number is not the maximum negative integer:
	    	largest_smallest_integers({i}).at(0) = -1; // then, return max of negative numbers;
	    }           // End of conditionals:
	}          // End of if-else:
	return {lst[0]};                        // Else, return the first element in list;
}
/* Output
largest_smallest_integers({2, 4, 1, 3, 5