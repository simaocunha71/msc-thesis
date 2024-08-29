#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<float> get_positive(vector<float> l){
    vector<float> ret;
    for (int i=0;i<l.size();i++){
        if (l[i]>0){
            ret.push_back(l[i]);
        }
    }
    return ret;
}
B:
/*
Return only positive numbers in the vector.
>>> get_positive({-1, 2, -4, 5, 6})
{2, 5, 6}
>>> get_positive({5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10})
{5, 3, 2, 3, 9, 123, 1}
*/
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
vector<float> get_positive(vector<float> l){
    vector<float> ret;
    for (int i=0;i<l.size();i++){
        if (l[i]>0){
            ret.push_back(l[i]);
        }
    }
    return ret;
}
C:
/*
Return only positive numbers in the vector.
>>> get_positive({-1, 2, -4, 5, 6})
{2, 5, 6}
>>> get_positive({5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10})
{5, 3, 2