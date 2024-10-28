    if(a.size()!=b.size()){
        return "Invalid Input";
    }
    for(int i=0;i<a.size();i++){
        if(a[i]=='0' && b[i]=='0'){
            a[i]='0';
        }else if(a[i]=='1' && b[i]=='1'){
            a[i]='0';
        }else if(a[i]=='0' && b[i]=='1'){
            a[i]='1';
        }else if(a[i]=='1' && b[i]=='0'){
            a[i]='1';
        }
    }
    return a;
}

int main() {
    string a,b;
    cin>>a>>b;
    cout<<string_xor(a,b);
    return 0;
}


/*
Input are two strings a and b consisting only of 1s and 0s.
Perform binary XOR on these inputs and return result also as a string.
>>> string_xor("010", "110")
"100"
*/
#include<stdio.h>
#include<string>
using namespace std;
string string_xor(string a,string b){

    if(a.size()!=b.size()){
        return "Invalid Input";
    }
    for(int i=0;i<a.size();i++){
        if(a[i]=='0' && b[i]=='0'){
            a[i]='0';
        }else if(a[i]=='1' && b[i]=='1'){
            a[i]='0';
        }else if(a[i]=='0' && b[i]=='1'){
            a[i]='1';
        }else if(a[i]=='1' && b[i]=='0'){
            a[i]='1';
        }
    }
    return a;
}

int main()