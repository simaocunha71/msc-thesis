    int count = 0;
    for(int i=11; i<n; i++){
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
int main(){
    int n;
    printf("Enter a number: ");
    scanf("%d",&n);
    printf("Count of 7's: %d", fizz_buzz(n));
    return 0;
}
*/

#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;

int fizz_buzz(int n){
    int count = 0;
    for(int i=11; i<n; i++){
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

int main(){
    int n;
    printf("Enter a number: ");
    scanf("%d",&n);
    printf("Count of 7's: %d", fizz_buzz(n));
    return 0;
}

*/

