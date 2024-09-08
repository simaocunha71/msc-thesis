    int sum = 0;
    for(int i = 0; i < s.length(); i++){
        if(isupper(s[i])){
            sum += int(s[i]);
        }
    }
    return sum;
} // Function to calculate the sum of ASCII values of upper case characters in a given string.

int main(){
    string s1 = "abAB";
    string s2 = "abcCd";
    string s3 = "helloE";
    string s4 = "woArBld";
    string s5 = "aAaaaXa";
    printf("digitSum(\"%s\") => %d\n", s1.c_str(), digitSum(s1));
    printf("digitSum(\"%s\") => %d\n", s2.c_str(), digitSum(s2));
    printf("digitSum(\"%s\") => %d\n", s3.c_str(), digitSum(s3));
    printf("digitSum(\"%s\") => %d\n", s4.c_str(), digitSum(s4));
    printf("digitSum(\"%s\") => %d\n", s5.c_str(), digitSum(s5));
    return 0;
} // Main function to test the digitSum function.

C:
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int digitSum(char *s) {
    int sum = 0;
    while (*s) {
        if (isupper(*s)) {
            sum += (int)*s;
        }
        s++;
    }
    return sum;
}

int main() {
    char *s1 = "abAB";
    char *s2 = "abcCd";
    char *s3 = "helloE";
    char *s4 = "woArBld";
    char *s5 = "aAaaaXa";
    printf("digitSum(\"%s\") => %d\n", s1, digitSum(s1));
    printf("digitSum(\"%s\") => %d\n", s2, digitSum(s2));
    printf("digitSum(\"%s\") => %d\n", s3, digitSum(s3));
    printf("digitSum(\"%s\") => %d\n", s4, digitSum(s4));
    printf("digitSum(\"%s\") => %d\n", s5, digitSum(s5));
    return 0;
} // Main function to test the digitSum function.