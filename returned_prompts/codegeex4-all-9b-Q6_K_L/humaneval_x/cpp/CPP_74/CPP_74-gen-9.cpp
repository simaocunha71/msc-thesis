#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
int count_chars(vector<string> lst){
    int cnt=0;
    for(int i=0;i<lst.size();i++){
        for(int j=0;j<lst[i].size();j++){
            cnt++;
        }
    }
    return cnt;
}
vector<string> total_match(vector<string> lst1,vector<string> lst2){
    int cnt1=count_chars(lst1);
    int cnt2=count_chars(lst2);
    if(cnt1==cnt2){
        return lst1;
    }
    else if(cnt1<cnt2){
        return lst1;
    }
    else{
        return lst2;
    }
}
B:
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
int count_chars(vector<string> lst){
    int cnt=0;
    for(int i=0;i<lst.size();i++){
        for(int j=0;j<lst[i].size();j++){
            cnt++;
        }
    }
    return cnt;
}
vector<string> total_match(vector<string> lst1,vector<string> lst2){
    int cnt1=count_chars(lst1);
    int cnt2=count_chars(lst2);
    if(cnt1>cnt2){
        return lst1;
    }
    else if(cnt1==cnt2){
        return lst1;
    }
    else{
        return lst2;
    }
}
C:
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
int count_chars(vector<string> lst){
    int cnt=0;
    for(int i=0;i<lst.size();i++){
        for(int j=0;j<lst[i].size();j++){
            cnt++;
        }
    }
    return cnt;
}
vector<string> total_match(vector<string> lst1,vector<string> lst2){
    int cnt1=count_chars(lst1);
    int cnt2=count_chars(lst2);
    if(cnt1<cnt2){
        return lst1;
    }
    else if(cnt1>cnt2){
        return lst1;
    }
    else{
        return lst1;
    }
}
D:
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
int count_chars(vector<string> lst){
    int cnt=0;
    for(int i=0;i<lst.size();i++){
        for(int j=0;j<lst[i].size();j++){
            cnt++;
        }
    }
    return cnt;
}
vector<string> total_match(vector