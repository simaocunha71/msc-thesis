    int sum=0;
    for (int i=1;i<lst.size();i++)
    if (lst[i]%2==0)
    sum+=lst[i];
    return sum;
}#include<stdio.h>
#include<vector>
using namespace std;
int add(vector<int> lst){
    int sum=0;
    for (int i=1;i<lst.size();i++)
    if (lst[i]%2==0)
    sum+=lst[i];
    return sum;
}
