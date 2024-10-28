
#include<bits/stdc++.h>
using namespace std;
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,a) FOR(i,0,a)
int main(){
    vector<int> lst = {0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3};
    int max = -1;
    for(int i:lst) max = max>i?max:i;
    int sum = 0;
    while(max>0) sum += max%10, max/=10;
    printf("%d\n",sum);
    return 0;
}

```