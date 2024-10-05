    int count = 0;
    transform(num.begin(), num.end(), num.begin(), ::toupper);
    for(int i = 0; i<num.size(); i++){
        if(num[i] == '2' || num[i] == '3' || num[i] == '5' || num[i] == '7' || num[i] == 'B' || num[i] == 'D'){
            count++;
        }
    }
    return count;
}

int main(){
    string num;
    printf("Enter a hexadecimal number: ");
    scanf("%s", &num);
    int res = hex_key(num);
    printf("Number of hexadecimal digits that are primes: %d", res);
    return 0;
}

*/
#include <stdio.h>

int hex_key(char *num) {
    int count = 0;
    for (int i = 0; num[i] != '\0'; i++) {
        switch (num[i]) {
            case '2':
            case '3':
            case '5':
            case '7':
            case 'B':
            case 'D':
                count++;
                break;
        }
    }
    return count;
}

int main() {
    char num[20];
    printf("Enter a hexadecimal number: ");
    scanf("%s", num);
    int res = hex_key(num);
    printf("Number of hexadecimal digits that are primes: %d", res);
    return 0;
}
/*
