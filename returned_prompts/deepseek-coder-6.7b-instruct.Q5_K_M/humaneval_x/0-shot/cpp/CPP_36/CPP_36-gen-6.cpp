    int i, count = 0, rem;
    for(i=0; i<n; i++){
        if(i%11 == 0 || i%13 == 0){
            while(i){
                rem = i%10;
                if(rem == 7)
                    count++;
                i = i/10;
            }
        }
    }
    return count;
}
int main(){
    int n;
    printf("Enter the number: ");
    scanf("%d",&n);
    printf("%d",fizz_buzz(n));
    return 0;
}

*/

/*
//Alternative solution with a little bit optimized
#include <stdio.h>

int fizz_buzz(int n){
    int i, count = 0;
    for(i=11; i<n; i+=11){
        if((i%10 == 7) || (i/10 == 7))
            count++;
    }
    for(i=13; i<n; i+=13){
        if((i%10 == 7) || (i/10 == 7))
            count++;
    }
    return count;
}

int main(){
    int n;
    printf("Enter the number: ");
    scanf("%d",&n);
    printf("%d",fizz_buzz(n));
    return 0;
}
*/

//C++/Fizz_buzz.cpp
/*

