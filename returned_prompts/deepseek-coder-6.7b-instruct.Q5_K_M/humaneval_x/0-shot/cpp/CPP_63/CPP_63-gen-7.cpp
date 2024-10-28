    if(n==0){
        return 0;
    }
    if(n==1){
        return 0;
    }
    if(n==2){
        return 1;
    }
    int fibfibNums[n+1];
    fibfibNums[0]=0;
    fibfibNums[1]=0;
    fibfibNums[2]=1;
    for(int i=3;i<=n;i++){
        fibfibNums[i]=fibfibNums[i-1]+fibfibNums[i-2]+fibfibNums[i-3];
    }
    return fibfibNums[n];
}

int main(){
    int n;
    scanf("%d",&n);
    printf("%d",fibfib(n));
    return 0;
}
*/

//C++ Program
#include<bits/stdc++.h>
using namespace std;

int fibfib(int n) {
    if(n == 0) {
        return 0;
    }
    if(n == 1) {
        return 0;
    }
    if(n == 2) {
        return 1;
    }
    vector<int> fibfibNums(n+1);
    fibfibNums[0] = 0;
    fibfibNums[1] = 0;
    fibfibNums[2] = 1;
    for(int i = 3; i <= n; i++) {
        fibfibNums[i] = fibfibNums[i-1] + fibfibNums[i-2] + fibfibNums[i-3];
    }
    return fibfibNums[n];
}

int main() {
    int n;
    cin >> n;
    cout << fibfib(n);
    return 0;
}
```

In this program, we first check if `n` is 0, 1, or 2. If it is, we return the corresponding