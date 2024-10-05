    vector<int> result;
    if(need <= remaining){
        result.push_back(number + need);
        result.push_back(remaining - need);
    }else{
        result.push_back(number + remaining);
        result.push_back(0);
    }
    return result;
}
*/

int main() {
    vector<int> result;
    result = eat(5, 6, 10);
    printf("[%d, %d]\n", result[0], result[1]);
    result = eat(4, 8, 9);
    printf("[%d, %d]\n", result[0], result[1]);
    result = eat(1, 10, 10);
    printf("[%d, %d]\n", result[0], result[1]);
    result = eat(2, 11, 5);
    printf("[%d, %d]\n", result[0], result[1]);
    return 0;
}#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LEN 1000

// 숫자인지 확인하는 함수
int isNum(char c) {
    return '0' <= c && c <= '9';
}

// 문자열의 길이를 반환하는 함수
int len(char *str) {
    int len = 0;
    while (str[len] != '\0') {
        len++;
    }
    return len;
}

// 문자열 뒤집는 함수
void reverse(char *str) {
    int l = len(str);
    for (int i = 0; i < l / 2; i++) {
        char temp = str[i];
       