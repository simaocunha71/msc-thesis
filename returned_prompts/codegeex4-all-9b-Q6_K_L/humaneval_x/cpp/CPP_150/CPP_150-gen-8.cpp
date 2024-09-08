    if(n<2){
        return y;
    }
    else{
        for(int i=2;i<n;i++){
            if(n%i==0){
                return y;
            }
        }
        return x;
    }

}
int main(){
    printf("%d\n",x_or_y(7, 34, 12));
    printf("%d\n",x_or_y(15, 8, 5));

    return 0;
} 

B:
#include<stdio.h>
using namespace std;
int x_or_y(int n,int x,int y){
    if(n<2){
        return y;
    }
    else if(n==2){
        return x;
    }
    else{
        for(int i=2;i<n;i++){
            if(n%i==0){
                return y;
            }
        }
        return x;
    }

}
int main(){
    printf("%d\n",x_or_y(7, 34, 12));
    printf("%d\n",x_or_y(15, 8, 5));

    return 0;
} 

C:
#include<stdio.h>
using namespace std;
int x_or_y(int n,int x,int y){
    if(n<2){
        return y;
    }
    else if(n==2){
        return x;
    }
    else{
        for(int i=2;i<n/2;i++){
            if(n%i==0){
                return y;
            }
        }
        return x;
    }

}
int main(){
    printf("%d\n",x_or_y(7, 34, 12));
    printf("%d\n",x_or_y(15, 8, 5));

    return 0;
} 

D:
#include<stdio.h>
using namespace std;
int x_or_y(int n,int x,int y){
    if(n<2){
        return y;
    }
    else if(n==2){
        return x;
    }
    else{
        for(int i=2;i<=n;i++){
            if(n%i==0){
                return y;
            }
        }
        return x;
    }

}
int main(){
    printf("%d\n",x_or_y(7, 34, 12));
    printf("%d\n",x_or_y(15, 8, 5));

    return 0;
} 

E:
#include<stdio.h>
using namespace std;
int x_or_y(int n,int x,int y){
    if(n<2){
        return y;
    }
    else