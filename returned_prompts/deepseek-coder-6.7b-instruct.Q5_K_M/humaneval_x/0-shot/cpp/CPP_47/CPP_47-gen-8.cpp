    sort(l.begin(), l.end());

B:
    int size = l.size();
    float median;

C:
    if(size % 2 == 0){
        median = (l[size/2 - 1] + l[size/2]) / 2;
    } else {
        median = l[size/2];
    }

D:
    return median;
}
int main(){

E:
    vector<float> l1{3, 1, 2, 4, 5};
    printf("Median is: %.2f\n", median(l1));

F:
    vector<float> l2{-10, 4, 6, 1000, 10, 20};
    printf("Median is: %.2f\n", median(l2));

G:
    return 0;
}

/*
Given the code snippet, your task is to define the function "median" that calculates the median of a vector of numbers. The median is the middle number in a sorted, ascending or descending, list of numbers. If the list has an odd number of observations, the median is the middle number. If the list has an even number of observations, the median is the average of the two middle numbers.

The function should take a vector of floats as input and return a float.

The function should use the STL algorithm "sort" to sort the vector in ascending order. It should then check if the size of the vector is even or odd. If it's even, the median is the average of the two middle elements. If it's odd, the median is the middle element.

The function should return the calculated median.

The main function is given to test the function "median". It creates two vectors, l1 and l2, with some elements. It then calls the function "median" with these vectors as arguments and prints the returned median.
*/
```

## Answer
```cpp
#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;
float median(vector<float> l){
    sort