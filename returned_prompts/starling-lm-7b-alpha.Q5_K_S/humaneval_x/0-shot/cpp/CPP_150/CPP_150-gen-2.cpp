    if(n==2){
        return x;
    }
    else if(n<2){
        return y;
    }
    else if(n%2==0){
        return y;
    }
    else if(n%2!=0){
        goto A;
    }
}

int main(){
    int x = 34;
    int y = 12;
    int n = 7;
    printf("%d\n",x_or_y(n,x,y));
    return 0;
}

*/
#include <bits/stdc++.h>
using namespace std;

int x_or_y(int n, int x, int y) {
    if (n == 2) {
        return x;
    } else if (n < 2) {
        return y;
    } else if (n % 2 == 0) {
        return y;
    } else if (n % 2 != 0) {
        return x;
    }
}

int main() {
    int x = 34;
    int y = 12;
    int n = 7;
    printf("%d\n", x_or_y(n, x, y));
    return 0;
}












































































































































































































