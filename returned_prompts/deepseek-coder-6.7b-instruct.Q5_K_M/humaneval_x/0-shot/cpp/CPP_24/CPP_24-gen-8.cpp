    for(int i = n-1; i > 0; i--){
        if(n % i == 0){
            return i;
        }
    }
}

int main(){
    printf("%d\n", largest_divisor(15));
    return 0;
}

#include<stdio.h>
int largest_divisor(int n){
    for(int i = n-1; i > 0; i--){
        if(n % i == 0){
            return i;
        }
    }
}
int main(){
    printf("%d\n", largest_divisor(15));
    return 0;
}

