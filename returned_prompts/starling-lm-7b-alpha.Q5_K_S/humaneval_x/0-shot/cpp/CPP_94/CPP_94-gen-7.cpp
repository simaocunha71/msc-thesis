    int i,max=0;
    for(i=0;i<lst.size();i++){
        if(lst[i]>max) max=lst[i];
    }

    if(max%2==0) return A(lst);
    if(max%2!=0) return B(lst);

    B:
    int n=max;
    int sum=0;
    while(n>0){
        sum+=n%10;
        n/=10;
    }
    return sum;
}

int main(){
    vector<int> lst;
    int i,n;
    scanf("%d",&n);
    for(i=0;i<n;i++){
        int x;
        scanf("%d",&x);
        lst.push_back(x);
    }
    printf("%d\n",skjkasdkd(lst));
}




































*/
#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> lst;
    int n,i;
    scanf("%d",&n);
    for(i=0;i<n;i++){
        int x;
        scanf("%d",&x);
        lst.push_back(x);
    }
    printf("%d\n",skjkasdkd(lst));
    return 0;
}

```