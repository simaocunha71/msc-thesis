/*
Return sorted unique common elements for two vectors.
>>> common({1, 4, 3, 34, 653, 2, 5}, {5, 7, 1, 5, 9, 653, 121})
{1, 5, 653}
>>> common({5, 3, 2, 8}, {3, 2})
{2, 3}

*/
#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> common(vector<int> l1,vector<int> l2){
    vector<int> v1;
    vector<int> v2;
    vector<int> result;
    for(int i=0;i<l1.size();i++)
    {
        int flag=1;
        for(int j=0;j<l2.size();j++)
        {
            if(l1[i]==l2[j])
            {
                flag=0;
                break;
            }
        }
        if(flag)
            v1.push_back(l1[i]);
    }
    for(int i=0;i<l2.size();i++)
    {
        int flag=1;
        for(int j=0;j<l1.size();j++)
        {
            if(l2[i]==l1[j])
            {
                flag=0;
                break;
            }
        }
        if(flag)
            v2.push_back(l2[i]);
    }
    int size1=v1.size();
    int size2=v2.size();
    int i=0,j=0;
    while(i<size1&&j<size2)
    {
        if(v1[i]<v2[j])
        {
            result.push_back(v1[i]);
            i++;
        }
        else if(v1[i]>v2[j])
        {
            result.push_back(v2[j]);
            j++;
        }
        else
        {
            result.push_back(v1[i]);
            i++;
            j++;
        }
    }
    while(i<size1)
    {
        result.push_back(v1[i]);
        i++;
    }
    while(j<size2)
    {
        result.push_back(v2[j]);
        j++;
    }
    return result;
}
int main()
{
    vector<int> l1={1, 4, 3, 34, 653, 2, 5};
    vector<int> l2={5, 7, 1, 5, 9, 653,