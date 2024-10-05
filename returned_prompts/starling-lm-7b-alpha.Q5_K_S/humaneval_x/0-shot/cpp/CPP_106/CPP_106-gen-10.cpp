#include<stdio.h>
#include<vector>
using namespace std;
vector<int> f(int n)
{
    vector<int> arr(n);
    for(int i=0;i<n;i++)
    {
        if(i%2==0)
        {
            arr[i]=i;
            for(int j=i;j>1;j--)
                arr[i]*=j;
        }
        else
        {
            int sum=0;
            for(int j=1;j<=i;j++)
                sum+=j;
            arr[i]=sum;
        }
    }
    return arr;
}
int main()
{
    int n;
    scanf("%d",&n);
    vector<int> arr=f(n);
    for(int i=0;i<n;i++)
        printf("%d ",arr[i]);
    return 0;
}












































































