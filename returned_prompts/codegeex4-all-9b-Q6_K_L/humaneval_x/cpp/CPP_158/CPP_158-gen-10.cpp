#include<stdio.h>
#include<math.h>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
string find_max(vector<string> words){
    int max=0;
    string ans="";
    for(int i=0;i<words.size();i++){
        vector<char> unique;
        int len=words[i].length();
        for(int j=0;j<len;j++){
            char temp=words[i][j];
            int flag=1;
            for(int k=0;k<unique.size();k++){
                if(temp==unique[k]){
                    flag=0;
                    break;
                }
            }
            if(flag==1){
                unique.push_back(temp);
            }
        }
        if(unique.size()>max){
            max=unique.size();
            ans=words[i];
        }
    }
    return ans;
}
B:
#include<stdio.h>
#include<math.h>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
string find_max(vector<string> words){
    int max=0;
    string ans="";
    for(int i=0;i<words.size();i++){
        vector<char> unique;
        int len=words[i].length();
        for(int j=0;j<len;j++){
            char temp=words[i][j];
            int flag=0;
            for(int k=0;k<unique.size();k++){
                if(temp==unique[k]){
                    flag=1;
                    break;
                }
            }
            if(flag==0){
                unique.push_back(temp);
            }
        }
        if(unique.size()>max){
            max=unique.size();
            ans=words[i];
        }
    }
    return ans;
}
C:
#include<stdio.h>
#include<math.h>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
string find_max(vector<string> words){
    int max=0;
    string ans="";
    for(int i=0;i<words.size();i++){
        vector<char> unique;
        int len=words[i].length();
        for(int j=0;j<len;j++){
            char temp=words[i][j];
            int flag=0;
            for(int k=0;k<unique.size();k++){
                if(temp==unique[k]){
                    flag=1;
                    break;
                }
            }
            if(flag==0){
                unique.push_back(temp);
            }
        }
        if(unique.size()>max){
            max=unique.size();
            ans=words[i];
        }
    }
    return ans;
}
D