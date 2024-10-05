    string binary = "";
    while (N > 0){
        binary = to_string(N % 2) + binary;
        N /= 2;
    }
    return binary;
}

int main(){
    int N;
    scanf("%d", &N);
    string out_ = solve(N);
    printf("%s", out_.c_str());
}
*/

//src/main.cpp
#include<iostream>
#include<string>
using namespace std;

int main(){
    string binary = "";
    int N;
    cin >> N;
    while (N > 0){
        binary = to_string(N % 2) + binary;
        N /= 2;
    }
    cout << binary << "\n";
    return 0;
}#include<stdio.h>
#include<stdlib.h>
#include<string.h>

char* solve(int N){
    char* binary = (char*)malloc(sizeof(char) * 32);
    int i = 0;
    while (N > 0){
        binary[i] = '0' + N % 2;
        N /= 2;
        i++;
    }
    binary[i] = '\0';
    // Reverse the binary string
    int start = 0, end = i - 1;
    while (start < end){
        char temp = binary[start];
        binary[start] = binary[end];
        binary[end] = temp;
        start++;
        end--;
    }
    return binary;
}

int main(){
    int N;
    scanf("%d", &N);
    char* out_ = solve(N);
    printf("%s\n", out_);
    free(out_);
    return 0;
}#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x, y;
    printf("Digite o primeiro numero: ");
    scanf("%d", &x);
    printf("Digite o segundo numero: ");
    scanf