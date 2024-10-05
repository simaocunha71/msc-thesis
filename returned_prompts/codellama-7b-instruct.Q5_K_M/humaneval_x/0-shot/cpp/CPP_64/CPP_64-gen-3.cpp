    int count = 0;
    for(int i = 0; i < s.size(); i++){
        if(s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u')
            count++;
        if(s[i] == 'y' && i == s.size() - 1)
            count++;
    }
    return count;
}
int main(){
    string a = "abcde";
    string b = "ACEDY";
    printf("%d\n", vowels_count(a));
    printf("%d\n", vowels_count(b));
}

Ans: C: 
/*
#include<stdio.h>
#include<string>
using namespace std;
int vowels_count(string s){
    int count = 0;
    for(int i = 0; i < s.size(); i++){
        if(s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u' || (s[i] == 'y' && i == s.size() - 1))
            count++;
    }
    return count;
}
int main(){
    string a = "abcde";
    string b = "ACEDY";
    printf("%d\n", vowels_count(a));
    printf("%d\n", vowels_count(b));
}
*/

