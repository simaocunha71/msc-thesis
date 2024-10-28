    vector<int> l_;
    for(int i=0; i<l.size(); i++){
        if(i%3!=0){
            l_.push_back(l[i]);
        }
    }
    sort(l_.begin(), l_.end());
    int i=0;
    for(int j=0; j<l.size(); j++){
        if(j%3!=0){
            l_[i++]=l[j];
        }
    }
    return l_;

}

Answer:A
*/

/*
This function takes two vectors, a and b, and returns the product of the corresponding elements of the two vectors, summed over all elements of the vectors.
For example, if a=[1, 2, 3] and b=[4, 5, 6], then the function should return 36, since 1*4 + 2*5 + 3*6 = 36.
>>> product_vectors({1, 2, 3}, {4, 5, 6})
36
>>> product_vectors({-1, -2, -3}, {4, 5, 6})
-33
*/

#include<stdio.h>
#include<vector>
using namespace std;
int product_vectors(vector<int> a, vector<int> b){
    int sum=0;
    for(int i=0; i<a.size(); i++){
        sum+=a[i]*b[i];
    }
    return sum;
}
Answer:

/*
This function takes two vectors a and b, and a scalar k. It returns a vector that is the result of adding the corresponding elements of a and b, scaled by k.
For example, if a=[1, 2, 3], b=[4, 5, 6] and k=2, then the function should return [2, 4, 6], since each element of a is increased by twice the corresponding element of b.
>>> add_scale({1, 2, 3}, {4, 5, 6}, 2)
{2, 4, 6}
>>> add_scale({