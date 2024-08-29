#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<assert.h>
#include<stdbool.h>

bool is_multiply_prime(int a){
    int prime[10]={2,3,5,7,11,13,17,19,23,29};
    int i=0;
    int j=0;
    int count=0;
    int flag=0;
    while(prime[i]!=0){
        j=0;
        while(prime[j]!=0){
            if(a==prime[i]*prime[j]){
                return true;
                break;
            }
            j++;
        }
        i++;
    }
    return false;
}
int main(){
    int a=30;
    if(is_multiply_prime(a))
        printf("True");
    else
        printf("False");
    return 0;
}

B:
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<assert.h>
#include<stdbool.h>

bool is_multiply_prime(int a){
    int prime[10]={2,3,5,7,11,13,17,19,23,29};
    int i=0;
    int j=0;
    int count=0;
    int flag=0;
    while(prime[i]!=0){
        j=0;
        while(prime[j]!=0){
            if(a==prime[i]*prime[j]){
                count++;
                if(count==3){
                    return true;
                    break;
                }
            }
            j++;
        }
        i++;
    }
    return false;
}
int main(){
    int a=30;
    if(is_multiply_prime(a))
        printf("True");
    else
        printf("False");
    return 0;
}

C:
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<assert.h>
#include<stdbool.h>

bool is_multiply_prime(int a){
    int prime[10]={2,3,5,7,11,13,17,19,23,29};
    int i=0;
    int j=0;
    int count=0;
    int flag=0;
    while(prime[i]!=0){
        j=0;
        while(prime[j]!=0){
            if(a==prime[i]*prime[j]){
                flag=1;
                break;
            }
            j++;
        }
        i++;
    }
    if(flag==1){
        return true;
    }
    else{
        return false;
    }
}
int main(){
   