    int count = 0;
    for(int i=0; i<n; i++){
        if(i%11 == 0 || i%13 == 0){
            char buffer[50];
            sprintf(buffer, "%d", i);
            for(int j=0; buffer[j] != '\0'; j++){
                if(buffer[j] == '7'){
                    count++;
                    break;
                }
            }
        }
    }
    return count;
}

int main(){
    printf("%d\n", fizz_buzz(50));
    printf("%d\n", fizz_buzz(78));
    printf("%d\n", fizz_buzz(79));
    return 0;
}




A: If you want to make it more efficient, you can avoid using the string conversion of the numbers and instead use the modulo operation to get the digits of the number. Here is a version of your function with this optimization:

```cpp
int count_sevens(int n){
    int count = 0;
    for(int i=0; i<n; i++){
        if(i%11 == 0 || i%13 == 0){
            int num = i;
            while(num > 0){
                if(num % 10 == 7){
                    count++;
                    break;
                }
                num /= 10;
            }
        }
    }
    return count;
}
```

This version of the function works by dividing the number by 10 at each step of the loop until the number is 0. The remainder of the division operation gives the last digit of the number. If this digit is 7, the function increments the count and breaks out of the loop. If not, the function removes the last digit of the number for the next iteration. This way, the function avoids the need to convert the number to a string and can therefore be more efficient.

Note: This version of the function still has a time complexity of O(n).

This version of the function should give the same results as your original function, but it should be more efficient.


A: