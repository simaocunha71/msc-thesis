    vector<float> l;
    vector<float> l1;
    int i=0;
    int j=0;
    int n=l.size();
    vector<float> l2;
    for(i=0;i<n;i++)
    {
        if(i%2==0)
        l1.push_back(l[i]);
    }
    sort(l1.begin(),l1.end());
    for(i=0;i<n;i++)
    {
        if(i%2!=0)
        l2.push_back(l1[j]);
        j++;
    }
    return l2;
}

/*
This function takes a vector l and returns a vector l' such that
l' is identical to l in the odd indicies, while its values at the even indicies are equal
to the values of the even indicies of l, but sorted.
>>> sort_even({1, 2, 3})
{1, 2, 3}
>>> sort_even({5, 6, 3, 4})
{3, 6, 5, 4}
*/

#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<float> sort_even(vector<float> l){

    vector<float> l;
    vector<float> l1;
    int i=0;
    int j=0;
    int n=l.size();
    vector<float> l2;
    for(i=0;i<n;i++)
    {
        if(i%2==0)
        l1.push_back(l[i]);
    }
    sort(l1.begin(),l1.end());
    for(i=0;i<n;i++)
    {
        if(i%2!=0)
        l2.push_back(l1[j]);
        j++;
    }
    return l2;
}
