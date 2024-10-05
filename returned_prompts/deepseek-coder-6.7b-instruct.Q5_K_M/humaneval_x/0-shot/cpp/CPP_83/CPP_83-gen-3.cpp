    int count = 0;
    if(n == 1){
        return 2;
    }
    else{
        count = 2 * (n-1) + 10 * (n-1) * (n-2) / 2;
    }

    return count;
}

int main(){
    int num;
    printf("Enter the number: ");
    scanf("%d", &num);
    printf("Count of n-digit integers starting or ending with 1 is: %d", starts_one_ends(num));
    return 0;
}
*/

#include <stdio.h>

int starts_one_ends(int n){
    int count = 0;
    if(n == 1){
        return 2;
    }
    else{
        count = 2 * (n-1) + 10 * (n-1) * (n-2) / 2;
    }

    return count;
}

int main(){
    int num;
    printf("Enter the number: ");
    scanf("%d", &num);
    printf("Count of n-digit integers starting or ending with 1 is: %d", starts_one_ends(num));
    return 0;
}

//Q2.c
#include <stdio.h>

int starts_one_ends(int n){
    int count = 0;
    if(n == 1){
        return 2;
    }
    else{
        count = 2 * (n-1) + 10 * (n-1) * (n-2) / 2;
    }

    return count;
}

int main(){
    int num;
    printf("Enter the number: ");
    scanf("%d", &num);
    printf("Count of n-digit integers starting or ending with 1 is: %d", starts_one_ends(num));
    return 0;
}

//Q3.c
#include <stdio.h>

int starts_one_ends(int n){
    int count = 0;
    if(n == 1){
        return 2;
    }
