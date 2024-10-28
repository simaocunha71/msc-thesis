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
```

The function digitSum() uses a for loop to traverse through each character in the string. If the character is uppercase, its ASCII value is added to the sum. The function returns the total sum.

The main() function tests the digitSum() function with a few test cases.

Note: In C++, the isupper() function is used to check if a character is uppercase.
*/

#include<stdio.h>
#include<string>
using namespace std;

int digitSum(string s){
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
```


In the test cases, the sum of the ASCII values of uppercase characters in the string "abAB" is 65 (A) + 65 (A) = 130. The sum of the ASCII values of uppercase characters in the string "abcCd" is 65 (A) + 67 (C) = 132. The sum of the ASCII values