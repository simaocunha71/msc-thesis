#include<stdio.h>
bool is_prime(int a){
    if(a<2){
        return false;
    }
    for(int i=2;i<a;i++){
        if(a%i==0){
            return false;
        }
    }
    return true;
}
bool is_multiply_prime(int a){
    int count=0;
    int product=1;
    for(int i=2;i<a;i++){
        if(is_prime(i)){
            count++;
            product*=i;
            if(count==3){
                break;
            }
        }
    }
    if(count==3 && product==a){
        return true;
    }
    else{
        return false;
    }
}
int main(){
    int a;
    printf("Enter a number: ");
    scanf("%d",&a);
    if(is_multiply_prime(a)){
        printf("%d is a multiplication of 3 prime numbers\n",a);
    }
    else{
        printf("%d is not a multiplication of 3 prime numbers\n",a);
    }
    return 0;
}

B:
#include<stdio.h>
#include<math.h>
bool is_prime(int a){
    if(a<2){
        return false;
    }
    for(int i=2;i<=sqrt(a);i++){
        if(a%i==0){
            return false;
        }
    }
    return true;
}
bool is_multiply_prime(int a){
    int count=0;
    int product=1;
    for(int i=2;i<a;i++){
        if(is_prime(i)){
            count++;
            product*=i;
            if(count==3){
                break;
            }
        }
    }
    if(count==3 && product==a){
        return true;
    }
    else{
        return false;
    }
}
int main(){
    int a;
    printf("Enter a number: ");
    scanf("%d",&a);
    if(is_multiply_prime(a)){
        printf("%d is a multiplication of 3 prime numbers\n",a);
    }
    else{
        printf("%d is not a multiplication of 3 prime numbers\n",a);
    }
    return 0;
}

C:
#include<stdio.h>
#include<math.h>
bool is_prime(int a){
    if(a<2){
        return false;
    }
    for(int i=2;i<=sqrt(a);i++){
        if(a%i==0){
            return false;
        }
    }
    return true;
}
bool is_multiply_prime(int a){
    int count=0;
    int product=1