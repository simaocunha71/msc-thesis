    if(arr.size()==0)
    return true;
    int i,j;
    bool flag=true;
    for(i=0;i<arr.size()-1;i++)
    {
        for(j=i+1;j<arr.size();j++)
        {
            if(arr[i]>arr[j])
            {
                flag=false;
                break;
            }
        }
        if(!flag)
        break;
    }
    return flag;
}
// or
#include<stdio.h>
#include<vector>
using namespace std;
bool move_one_ball(vector<int> arr){
    int i;
    for(i=0;i<arr.size()-1;i++)
    {
        if(arr[i]>arr[i+1])
        return false;
    }
    return true;
}