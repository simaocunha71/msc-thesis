for(int i=0;i<b.size();i++){
    string temp=b.substr(i)+b.substr(0,i);
    if(a.find(temp)!=string::npos){
        return true;
    }
}
return false;
}
int main(){
    printf("%d",cycpattern_check("abcd","abd"));
    printf("%d",cycpattern_check("hello","ell"));
    printf("%d",cycpattern_check("whassup","psus"));
    printf("%d",cycpattern_check("abab","baa"));
    printf("%d",cycpattern_check("efef","eeff"));
    printf("%d",cycpattern_check("himenss",'simen"));
    return 0;
}

Output:
0000101


A: Your question is a bit confusing. It seems like you want to check if the rotation of string b is a substring of string a.
If that is the case, your code is correct. 

However, the 'main' function does not return a boolean value. You need to print either 0 (for false) or 1 (for true) to represent a boolean value.

Here is the corrected code:

```cpp
#include<iostream>
#include<string>
using namespace std;

bool cycpattern_check(string a,string b){

    for(int i=0;i<b.size();i++){
        string temp=b.substr(i)+b.substr(0,i);
        if(a.find(temp)!=string::npos){
            return true;
        }
    }
    return false;
}

int main(){
    cout<<cycpattern_check("abcd","abd")<<endl;
    cout<<cycpattern_check("hello","ell")<<endl;
    cout<<cycpattern_check("whassup","psus")<<endl;
    cout<<cycpattern_check("abab","baa")<<endl;
    cout<<cycpattern_check("efef","eeff")<<end