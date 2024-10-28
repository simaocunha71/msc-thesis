    for(int j=0;j<b.size();j++){
        for(int i=0;i<a.size()-b.size()+1;i++){
            string temp=a.substr(i,b.size());
            for(int k=0;k<temp.size();k++){
                if(temp[(k+j)%b.size()]==b[k])continue;
                else break;
            }
            return true;
        }
    }
    return false;
}
int main(){
    string a,b;
    scanf("%s",&a);
    scanf("%s",&b);
    printf("%d",cycpattern_check(a,b));
    return 0;
}

This C++ code will check if the second word or any of its rotations is a substring in the first word. If any rotation is found, it will return true else false.

*/
#include<bits/stdc++.h>
using namespace std;
bool cycpattern_check(string a,string b){
    for(int j=0;j<b.size();j++){
        for(int i=0;i<a.size()-b.size()+1;i++){
            string temp=a.substr(i,b.size());
            for(int k=0;k<temp.size();k++){
                if(temp[(k+j)%b.size()]==b[k])continue;
                else break;
            }
            return true;
        }
    }
    return false;
}
int main(){
    string a,b;
    cin>>a>>b;
    cout<<cycpattern_check(a,b);
    return 0;
}

This C++ code will check if the second word or any of its rotations is a substring in the first word. If any rotation is found, it will return true else false.

*/
#include<bits/stdc++.h>
using namespace std;
bool cycpattern_check(string a,string b){
    for(int j=0;j<b.size();j++