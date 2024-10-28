    vector<int> result(2, 0);
    num = abs(num);
    while(num > 0){
        int digit = num % 10;
        if(digit % 2 == 0)
            result[0]++;
        else
            result[1]++;
        num /= 10;
    }
    return result;
}

int main(){
    int num;
    scanf("%d", &num);
    vector<int> result = even_odd_count(num);
    printf("%d %d\n", result[0], result[1]);
    return 0;
}

//This solution is for C++. If you want a C solution, it's a bit more complex because C doesn't have a built-in abs() function. Also, C doesn't support vectors like in C++, but you can use arrays.

C:

#include<stdio.h>
int main(){
    int num,even=0,odd=0;
    scanf("%d",&num);
    num = num < 0 ? -num : num;
    while(num>0){
        if((num%10)%2==0)
            even++;
        else
            odd++;
        num /= 10;
    }
    printf("%d %d\n",even,odd);
    return 0;
}

*/

//src/14.c
/*
