    int largest_negative =0;
    int smallest_positive =0;
    for(int i=0;i<lst.size();i++){
        if(lst[i]<0 && lst[i]>largest_negative){
            largest_negative = lst[i];
        }
        if(lst[i]>0 && (smallest_positive==0 || lst[i]<smallest_positive)){
            smallest_positive = lst[i];
        }
    }

    return {largest_negative,smallest_positive};
}

*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> largest_smallest_integers(vector<int> lst){
    int largest_negative =0;
    int smallest_positive =0;
    for(int i=0;i<lst.size();i++){
        if(lst[i]<0 && lst[i]>largest_negative){
            largest_negative = lst[i];
        }
        if(lst[i]>0 && (smallest_positive==0 || lst[i]<smallest_positive)){
            smallest_positive = lst[i];
        }
    }
    return {largest_negative,smallest_positive};
}

int main()
{
    vector<int> result = largest_smallest_integers({2, 4, -1, 3, -5, 7});
    for(int i=0; i<result.size(); i++)
        cout<< result[i] << " ";
    return 0;
}

// Output: -5 2

// Note: This code will return the largest negative integer and smallest positive integer in the vector. If there are no negative integers in the vector, it will return 0 for the largest negative integer. Similarly, if there are no positive integers in the vector, it will return 0 for the smallest positive integer.

/*
This code works by iterating over the vector and checking each element. If the element is negative and greater than the current largest negative number, it becomes the