    int sum = 0;
    for(int i=0; i<s.size(); i++){
        if(s[i] >= 'A' && s[i] <= 'Z'){
            sum += int(s[i]);
        }
    }
    return sum;
}

int main(){
    printf("%d\n",digitSum("abAB"));
    printf("%d\n",digitSum("abcCd"));
    printf("%d\n",digitSum("helloE"));
    printf("%d\n",digitSum("woArBld"));
    printf("%d\n",digitSum("aAaaaXa"));
    return 0;
}

*/

#include <iostream>
#include <cctype>
#include <string>
using namespace std;

int digitSum(string s){
    int sum = 0;
    for(int i=0; i<s.size(); i++){
        if(isupper(s[i])){
            sum += int(s[i]);
        }
    }
    return sum;
}

int main(){
    cout<<digitSum("abAB")<<endl;
    cout<<digitSum("abcCd")<<endl;
    cout<<digitSum("helloE")<<endl;
    cout<<digitSum("woArBld")<<endl;
    cout<<digitSum("aAaaaXa")<<endl;
    return 0;
}

/*
Output:
131
67
69
131
153
*/

//Task/Task4/task4.cpp
/*
Task
Write a program that takes a string as input and outputs the sum of ASCII values of all characters in the string.

Examples:
    digitSum("") → 0
    digitSum("abAB") → 131
    digitSum("abcCd") → 67
    digitSum("helloE") → 69
    digitSum("woArBld") → 131
    digitSum("aAaaaXa") →