#include<iostream>
#include<vector>
#include<string>
using namespace std;
string match_parens(vector<string> lst){
    int l1 = lst[0].length();
    int l2 = lst[1].length();
    int left = 0;
    int right = 0;
    for(int i = 0; i < l1; i++){
        if(lst[0][i] == '(') left++;
        else if(lst[0][i] == ')') right++;
    }
    for(int i = 0; i < l2; i++){
        if(lst[1][i] == '(') left++;
        else if(lst[1][i] == ')') right++;
    }
    if(left == right) return "Yes";
    else return "No";
}

B:
#include<iostream>
#include<vector>
#include<string>
using namespace std;
string match_parens(vector<string> lst){
    int l1 = lst[0].length();
    int l2 = lst[1].length();
    int left = 0;
    int right = 0;
    for(int i = 0; i < l1; i++){
        if(lst[0][i] == '(') left++;
    }
    for(int i = 0; i < l2; i++){
        if(lst[1][i] == ')') right++;
    }
    if(left == right) return "Yes";
    else return "No";
}

C:
#include<iostream>
#include<vector>
#include<string>
using namespace std;
string match_parens(vector<string> lst){
    int l1 = lst[0].length();
    int l2 = lst[1].length();
    int left = 0;
    int right = 0;
    for(int i = 0; i < l1; i++){
        if(lst[0][i] == '(') left++;
        else if(lst[0][i] == ')') right++;
    }
    for(int i = 0; i < l2; i++){
        if(lst[1][i] == '(') left++;
        else if(lst[1][i] == ')') right++;
    }
    if(left == right) return "Yes";
    else return "No";
}

D:
#include<iostream>
#include<vector>
#include<string>
using namespace std;
string match_parens(vector<string> lst){
    int l1 = lst[0].length();
    int l2 = lst[1