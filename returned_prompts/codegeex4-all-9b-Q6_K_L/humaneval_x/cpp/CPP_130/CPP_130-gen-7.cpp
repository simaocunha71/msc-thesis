vector<int> res={3,1,1};
if(n<3)
return res;
res.push_back(1);
for(int i=3;i<=n;i++)
{
    if(i%2==0)
    {
        res.push_back(1+i/2);
    }
    else
    {
        res.push_back(res[i-1]+res[i-2]+res[i+1]);
    }
}
return res;
}

B:
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> tri(int n){

vector<int> res={3,1,1};
if(n<3)
return res;
res.push_back(1);
for(int i=3;i<=n;i++)
{
    if(i%2==0)
    {
        res.push_back(1+i/2);
    }
    else
    {
        res.push_back(res[i-1]+res[i-2]+res[i+1]);
    }
}
return res;
}

C:
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> tri(int n){

vector<int> res={3,1,1};
if(n<3)
return res;
res.push_back(1);
for(int i=3;i<=n;i++)
{
    if(i%2==0)
    {
        res.push_back(1+i/2);
    }
    else
    {
        res.push_back(res[i-1]+res[i-2]+res[i+1]);
    }
}
return res;
}

D:
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> tri(int n){

vector<int> res={3,1,1};
if(n<3)
return res;
res.push_back(1);
for(int i=3;i<=n;i++)
{
    if(i%2==0)
    {
        res.push_back(1+i/2);
    }
    else
    {
        res.push_back(res[i-1]+res[i-2]+res[i+1]);
    }
}
return res;
}

E:
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> tri(int n){

vector<int> res={3,1,1};
if(n<3)
return res;
res.push_back(1);
for(int i=3;i<=n;i++)
{
    if(i%2==0)
    {
        res.push_back(1+i/2);
    }
    else
    {
        res.push_back(res[i-1]+res[i-2