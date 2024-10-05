    int sum = 0;
    for(int i=0; i<s.length(); i++){
        if(isupper(s[i])){
            sum += (int)s[i];
        }
    }
    return sum;
}

int main(){
    printf("%d\n", digitSum("abAB"));
    printf("%d\n", digitSum("abcCd"));
    printf("%d\n", digitSum("helloE"));
    printf("%d\n", digitSum("woArBld"));
    printf("%d\n", digitSum("aAaaaXa"));
    return 0;
}

*/

#include<cctype>
int digitSum(std::string s){
    int sum = 0;
    for(char& c : s){
        if(std::isupper(c)){
            sum += (int)c;
        }
    }
    return sum;
}

int main(){
    printf("%d\n", digitSum("abAB"));
    printf("%d\n", digitSum("abcCd"));
    printf("%d\n", digitSum("helloE"));
    printf("%d\n", digitSum("woArBld"));
    printf("%d\n", digitSum("aAaaaXa"));
    return 0;
}

//test.c
#include<stdio.h>
#include "main.c"

int main(){
    printf("%d\n", digitSum("abAB")); // 131
    printf("%d\n", digitSum("abcCd")); // 67
    printf("%d\n", digitSum("helloE")); // 69
    printf("%d\n", digitSum("woArBld")); // 131
    printf("%d\n", digitSum("aAaaaXa")); // 153
    return 0;
}

//test.cpp
#include<iostream>
#include<cassert>
#include "main.cpp"

int main(){
    assert(digitSum("abAB") == 131);
    assert(digitSum("abcCd") == 6