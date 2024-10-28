    int count=0;

B:
    for(int i=11;i<n;i++){
        if(i%11==0 || i%13==0){
            char buffer[50];
            sprintf(buffer, "%d", i);
            for(int j=0;buffer[j] != '\0';j++){
                if(buffer[j]=='7'){
                    count++;
                    break;
                }
            }
        }
    }
    return count;
}

int main(){
    int n=78;
    printf("%d\n",fizz_buzz(n));
    return 0;
}

*/

#include<stdio.h>
#include<stdlib.h>

int fizz_buzz(int n){
    int count=0, i, j, len;
    char *buffer;
    asprintf(&buffer, "%d", n);
    len = strlen(buffer);

    for(i=0; i<len; i++){
        if(buffer[i]=='7'){
            count++;
        }
    }

    free(buffer);

    return count;
}

int main(){
    printf("%d\n",fizz_buzz(78));
    printf("%d\n",fizz_buzz(79));
    return 0;
}

// C++ Version
#include<iostream>
#include<string>
using namespace std;

int fizz_buzz(int n){
    int count = 0;
    string buffer;

    for(int i=11; i<n; i++){
        if(i%11==0 || i%13==0){
            buffer = to_string(i);
            for(int j=0; j<buffer.size(); j++){
                if(buffer[j]=='7'){
                    count++;
                    break;
                }
            }
        }
    }
    return count;
}

int main(){
    cout << fizz_buzz(78