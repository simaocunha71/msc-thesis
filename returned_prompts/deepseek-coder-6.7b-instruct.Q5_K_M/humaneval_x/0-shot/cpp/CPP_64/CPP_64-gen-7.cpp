    int count = 0;
    for(int i=0; i<s.length(); i++){
        if(i==s.length()-1 && (s[i]=='y'||s[i]=='Y')){
            count++;
        }
        else if(s[i]=='a'||s[i]=='e'||s[i]=='i'||s[i]=='o'||s[i]=='u'||s[i]=='A'||s[i]=='E'||s[i]=='I'||s[i]=='O'||s[i]=='U'){
            count++;
        }
    }
    return count;
}

int main(){
    printf("%d", vowels_count("abcde"));
    printf("%d", vowels_count("ACEDY"));
    return 0;
}

*/

#include<bits/stdc++.h>
using namespace std;

int vowels_count(string s){
    int count = 0;
    for(int i=0; i<s.length(); i++){
        if(i==s.length()-1 && (s[i]=='y'||s[i]=='Y')){
            count++;
        }
        else if(s[i]=='a'||s[i]=='e'||s[i]=='i'||s[i]=='o'||s[i]=='u'||s[i]=='A'||s[i]=='E'||s[i]=='I'||s[i]=='O'||s[i]=='U'){
            count++;
        }
    }
    return count;
}

int main(){
    cout << vowels_count("abcde") << endl;
    cout << vowels_count("ACEDY") << endl;
    return 0;
}

*/

