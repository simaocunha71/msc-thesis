    if(s.length()<3){
        return false;
    }
    int n = s.length();
    for(int i=0;i<n-2;i++){
        char c1 = s[i];
        char c2 = s[i+1];
        char c3 = s[i+2];
        if(c1==c2||c2==c3||c1==c3){
            return false;
        }
    }
    return true;
}

int main(){
    string s;
    while(scanf("%s",s)!=EOF){
        if(is_happy(s)){
            printf("true\n");
        }else{
            printf("false\n");
        }
    }
    return 0;
}


*/
#include<set>
#include<cstdio>
#include<cstring>
#include<string>
#include<iostream>
using namespace std;

int main(){
    string s;
    while(cin>>s){
        if(s.length()<3){
            puts("false");
            continue;
        }
        set<char> st;
        int n = s.length();
        int flag = 0;
        for(int i=0;i<n-2;i++){
            if(st.find(s[i])!=st.end()){
                puts("false");
                flag = 1;
                break;
            }
            if(st.find(s[i+1])!=st.end()){
                puts("false");
                flag = 1;
                break;
            }
            if(st.find(s[i+2])!=st.end()){
                puts("false");
                flag = 1;
                break;
            }
            st.insert(s[i]);
            st.insert(s[i+1]);
            st.insert(s[i+2]);
        }
        if(flag==0) puts("true");
    }
    return 0;
}









