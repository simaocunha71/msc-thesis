    vector<int> v;
    for(int i=2;i<n;i++)
    {
        bool flag=true;
        for(int j=2;j*j<=i;j++)
        {
            if(i%j==0)
            {
                flag=false;
                break;
            }
        }
        if(flag)
        {
            v.push_back(i);
        }
    }
    return v;
}

int main()
{
    int n;
    scanf("%d",&n);
    vector<int> v;
    v=count_up_to(n);
    for(int i=0;i<v.size();i++)
    {
        printf("%d ",v[i]);
    }
    return 0;
}

*/
#include<iostream>
#include<vector>
using namespace std;
vector<int> count_up_to(int n){
    vector<int> v;
    for(int i=2;i<n;i++)
    {
        bool flag=true;
        for(int j=2;j*j<=i;j++)
        {
            if(i%j==0)
            {
                flag=false;
                break;
            }
        }
        if(flag)
        {
            v.push_back(i);
        }
    }
    return v;
}
int main()
{
    int n;
    cin>>n;
    vector<int> v;
    v=count_up_to(n);
    for(int i=0;i<v.size();i++)
    {
        cout<<v[i]<<" ";
    }
    return 0;
}



















































































