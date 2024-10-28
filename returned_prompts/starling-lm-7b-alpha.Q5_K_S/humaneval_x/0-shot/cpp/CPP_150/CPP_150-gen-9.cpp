    if(n==1){
        return y;
    }
    else if(n==2){
        return x;
    }
    else if(n%2==0){
        return y;
    }
    else{
        goto A;
    }
}

int main(){
    int x,y,n;
    scanf("%d%d%d",&n,&x,&y);
    printf("%d",x_or_y(n,x,y));
}






*/
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n,x,y;
    scanf("%d%d%d",&n,&x,&y);
    if(n==1){
        printf("%d",y);
    }
    else if(n==2){
        printf("%d",x);
    }
    else if(n%2==0){
        printf("%d",y);
    }
    else{
        printf("%d",x);
    }
    return 0;
}




























































































































































































































































