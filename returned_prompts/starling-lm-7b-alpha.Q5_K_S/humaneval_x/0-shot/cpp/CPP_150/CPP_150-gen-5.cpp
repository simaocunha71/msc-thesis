    if(n==0){
        return x;
    }
    if(n==1){
        return y;
    }
    for(int i=2;i<=n/2;i++){
        if(n%i==0){
            goto B;
        }
    }
    goto A;
    B:
        return y;
}

int main(){
    int x,y,n;
    scanf("%d %d %d",&n,&x,&y);
    printf("%d\n",x_or_y(n,x,y));
    return 0;
}














*/
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, x, y;
    scanf("%d %d %d", &n, &x, &y);
    int ans = x_or_y(n, x, y);
    printf("%d\n", ans);
    return 0;
}

int x_or_y(int n, int x, int y) {
    if (n == 0) {
        return x;
    }
    if (n == 1) {
        return y;
    }
    for (int i = 2; i <= n / 2; ++i) {
        if (n % i == 0) {
            return y;
        }
    }
    return x;
}





























































































































































