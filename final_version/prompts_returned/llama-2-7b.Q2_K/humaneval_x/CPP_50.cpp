#include<stdio.h>
#include<string>
using namespace std;
string encode_shift(string s){
    // returns encoded string by shifting every character by 5 in the alphabet.
    string out;
    int i;
    for (i=0;i<s.length();i++)
    {
        int w=((int)s[i]+5-(int)'a')%26+(int)'a';   
        out=out+(char)w;
    }
    return out;
}
string decode_shift(string s){
    // takes as input string encoded with encode_shift function. Returns decoded string.
    int i,j;
    string out;
    for (i = 0; i < s.length(); i++){
        j=0;  
        while(j<26 && s[i]-'a'!=j){
            j++;  
        }   
        int w=((int)s[i]+'a'-5-(int)'a')%26+(int)'a'; 
        out+=char('a'+w);        
    }
    return out;    
}
void encode_alphabet(string s){
    // takes alphabet as input and returns encoded string. Returns true iff all characters in the alphabet are less than 26.
    int i,j;
    string out;
    for (i = 0; i <26 ; i++) {  
        j=0;  
        while(j<5 && 'a'+w<s[i]){                     
            j++;      
        }              
        int w=((int)s[i]+'a'-5-(int)'a')%26+(int)'a'; 
        if (w == out.back()) {    //out.size() will always be even because every two characters are shifted by each other.  
            continue;    
        }
        else{          
             out+=char('a'+w);  
        }              
    }            
}
int main(void){
   string s="hello";
   encode_alphabet(s);  //encode_shift returns encoded string.
   printf("%s\n",decode_shift(encode