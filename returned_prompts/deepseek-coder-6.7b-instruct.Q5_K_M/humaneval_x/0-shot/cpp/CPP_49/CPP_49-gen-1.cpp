    if(n==0)
        return 1;
    else
        return (2 * modp(n-1,p)) % p;
}
int main(){
    int n,p;
    scanf("%d %d",&n,&p);
    printf("%d",modp(n,p));
    return 0;
}


A: In your code, you are trying to calculate 2^n mod p. But in your code, you are using the modulo operator (%) after multiplying 2 and before applying the modulo operator. This is not correct because the modulo operator has a higher precedence than the multiplication operator in C++. Therefore, you should calculate the modulo of 2^n before multiplying it with p.

Here is the corrected code:
#include<stdio.h>
using namespace std;
int modp(int n,int p){
    if(n==0)
        return 1;
    else
        return (modp(n-1,p)*2) % p;
}
int main(){
    int n,p;
    scanf("%d %d",&n,&p);
    printf("%d",modp(n,p));
    return 0;
}

This code will calculate 2^n mod p correctly.

A: The question is asking for a function that calculates 2^n mod p. The modulo operation is a mathematical operation that returns the remainder after division by a number.
Here is the corrected code:
#include<stdio.h>
using namespace std;

int modp(int n, int p){
    if(n == 0)
        return 1;
    else{
        int temp = modp(n/2, p);
        if(n % 2 == 0)
            return (temp * temp) % p;
        else
            return (2 * temp * temp) % p;
    }
}

int main(){
    int n, p;
    scanf("%d %d",&n,&p);
    printf("%d",modp(n, p));
    return 0;
}

This code will calculate 2^n mod p correctly