/*
Write a function vowels_count which takes a string representing a word as input and returns the number of vowels in the string. Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 
Here, 'y' is also a vowel, but only when it is at the end of the given word.
Example: 
>>> vowels_count("abcde") 
2 
>>> vowels_count("ACEDY") 
3
*/
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
int vowels_count(string s){
    int count=0;
    for(int i=0;i<s.length();i++){
        if(s[i]=='a'||s[i]=='e'||s[i]=='i'||s[i]=='o'||s[i]=='u'||s[i]=='y'){
            count++;
        }
    }
    if(s[s.length()-1]=='y'){
        count++;
    }
    return count;
}
int main(){
    string s;
    cout<<"Enter a string: ";
    cin>>s;
    cout<<"Number of vowels in the string: "<<vowels_count(s)<<endl;
    return 0;
}