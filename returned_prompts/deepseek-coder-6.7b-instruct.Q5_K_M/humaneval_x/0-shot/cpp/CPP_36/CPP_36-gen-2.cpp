    int count = 0;
    for(int i=1; i<n; i++){
        if(i%11==0 || i%13==0){
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

int main() {
    printf("%d\n", fizz_buzz(50));
    printf("%d\n", fizz_buzz(78));
    printf("%d\n", fizz_buzz(79));
    return 0;
}

*/

#include<stdio.h>
int fizz_buzz(int n){
    int count = 0;
    for(int i=1; i<n; i++){
        if(i%11==0 || i%13==0){
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

int main() {
    printf("%d\n", fizz_buzz(50));
    printf("%d\n", fizz_buzz(78));
    printf("%d\n", fizz_buzz(79));
    return 0;
}


*/

//cplusplus/src/exercise/sieve_eratosthenes.cpp
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<stdbool.h>
#include<string.h>


bool* sieve_of_eratosthenes(int n){
    bool* prime = (bool*)malloc((n+1)*sizeof(bool));
   