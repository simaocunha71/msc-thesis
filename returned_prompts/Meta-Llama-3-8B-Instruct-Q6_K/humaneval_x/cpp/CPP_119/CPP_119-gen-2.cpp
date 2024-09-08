    int count = 0;
    for(int i = 0; i < lst.size(); i++){
        for(int j = 0; j < lst[i].size(); j++){
            if(lst[i][j] == '('){
                count++;
            }
            else if(lst[i][j] == ')'){
                if(count > 0){
                    count--;
                }
                else{
                    return "No";
                }
            }
        }
    }
    if(count > 0){
        return "No";
    }
    else{
        return "Yes";
    }
}

int main(){
    vector<string> lst = {"()(", ")"};
    cout<<match_parens(lst)<<endl;
    return 0;
}

B:
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string match_parens(vector<string> lst){
    int count = 0;
    for(int i = 0; i < lst.size(); i++){
        for(int j = 0; j < lst[i].size(); j++){
            if(lst[i][j] == '('){
                count++;
            }
            else if(lst[i][j] == ')'){
                if(count > 0){
                    count--;
                }
                else{
                    return "No";
                }
            }
        }
    }
    if(count > 0){
        return "No";
    }
    else{
        return "Yes";
    }
}

int main(){
    vector<string> lst = {")("};
    cout<<match_parens(lst)<<endl;
    return 0;
}
C:
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string match_parens(vector<string> lst){
    int count = 0;
    for(int i = 0; i < lst.size(); i++){
        for(int j = 0; j < lst[i].size(); j++){
            if(lst[i][j] == '('){
                count++;
            }
            else if(lst[i][j] == ')'){
                if(count > 0){
                    count--;
                }
                else{
                    return "No";
                }
            }
        }
    }
    if(count > 0){
        return "No";
    }
    else{
        return "Yes";
    }
}

int main(){
    vector<string> lst = {"()("};
    cout<<match_parens(lst)<<endl;
    return 0;
}
D:
#include<stdio.h>
#include<vector>
#include<string>
using namespace std