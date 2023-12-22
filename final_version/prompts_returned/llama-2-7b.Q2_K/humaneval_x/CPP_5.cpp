/*
Insert a number "delimeter" between every two consecutive elements of input vector `numbers"
>>> intersperse({}, 4)
{}
>>> intersperse({1, 2, 3}, 4)
{1, 4, 2, 4, 3}
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> intersperse(vector<int> numbers, int delimeter){ 
	vector<int> temp_vec;  
    int i, j;
    for (i=0; i<numbers.size(); i++){
        if(!(i%delimeter)) { // Check if we are on the first or last position of the loop.
            if(!j){ 
                     temp_vec.push_back(numbers[i]);  
             } else {// Checks to see if the j-th element is equal with that in the vector. If so, it removes the j-th element and adds to vector a copy of numbers[i]
                for (j=0; j<i; j++) { // Goes through the vector from 0 to i-1.
                    if(temp_vec[i-1]==numbers[j]){// If we find the element equal with it, breaks the loop and does not add to temp_vec another copy of numbers[i].
                        break;
                }
            }}temp_vec.push_back(numbers[i]);
        }  else { // It doesn't print numbers if i is neither divisible by delimeter nor ends in it.
             j++;
        }  
    } return temp_vec;
}
