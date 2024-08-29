vector<int> v={3};
if(n==0) return v;
int a[n+1];
a[0]=3;
for(int i=1;i<=n;i++)
{
    if(i%2==0)
        a[i]=1+(i/2);
    else
        a[i]=a[i-1]+a[i-2]+a[i+1];
    v.push_back(a[i]);
}
return v;
}
B:
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> tri(int n){

vector<int> v={3};
if(n==0) return v;
int a[n+1];
a[0]=3;
for(int i=1;i<=n;i++)
{
    if(i%2==0)
        a[i]=1+(i/2);
    else
        a[i]=a[i-1]+a[i-2]+a[i+1];
    v.push_back(a[i]);
}
return v;
}
C:
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> tri(int n){

vector<int> v={3};
if(n==0) return v;
int a[n+1];
a[0]=3;
for(int i=1;i<=n;i++)
{
    if(i%2==0)
        a[i]=1+(i/2);
    else
        a[i]=a[i-1]+a[i-2]+a[i+1];
    v.push_back(a[i]);
}
return v;
}
D:
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> tri(int n){

vector<int> v={3};
if(n==0) return v;
int a[n+1];
a[0]=3;
for(int i=1;i<=n;i++)
{
    if(i%2==0)
        a[i]=1+(i/2);
    else
        a[i]=a[i-1]+a[i-2]+a[i+1];
    v.push_back(a[i]);
}
return v;
}
E:
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> tri(int n){

vector<int> v={3};
if(n==0) return v;
int a[n+1];
a[0]=3;
for(int i=1;i<=n;i++)
{
    if(i%2==0)
        a[i]=1+(i/2);
    else
        a[i]=a[i-1]+a[i-2