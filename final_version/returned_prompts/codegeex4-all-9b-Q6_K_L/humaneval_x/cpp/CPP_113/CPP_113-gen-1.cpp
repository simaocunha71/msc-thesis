#include<stdio.h>
#include<vector>
#include<string>
#include<map>
using namespace std;
vector<string> odd_count(vector<string> lst){
    vector<string> output;
    for(int i = 0;i<lst.size();i++){
        int count = 0;
        for(int j=0;j<lst[i].size();j++){
            if(int(lst[i][j])%2 != 0){
                count++;
            }
        }
        output.push_back("the number of odd elements in the string "+to_string(i)+" of the input.");
        output[i] = output[i].replace(output[i].find("i"),1,to_string(count));
    }
    return output;
}
B:
#include<stdio.h>
#include<vector>
#include<string>
#include<map>
using namespace std;
vector<string> odd_count(vector<string> lst){
    vector<string> output;
    for(int i = 0;i<lst.size();i++){
        int count = 0;
        for(int j=0;j<lst[i].size();j++){
            if(int(lst[i][j])%2 != 0){
                count++;
            }
        }
        output.push_back("the number of odd elements in the string "+to_string(i)+" of the input.");
        output[i] = output[i].replace(output[i].find("i"),1,to_string(count));
    }
    return output;
}
C:
#include<stdio.h>
#include<vector>
#include<string>
#include<map>
using namespace std;
vector<string> odd_count(vector<string> lst){
    vector<string> output;
    for(int i = 0;i<lst.size();i++){
        int count = 0;
        for(int j=0;j<lst[i].size();j++){
            if(int(lst[i][j])%2 != 0){
                count++;
            }
        }
        output.push_back("the number of odd elements in the string "+to_string(i)+" of the input.");
        output[i] = output[i].replace(output[i].find("i"),1,to_string(count));
    }
    return output;
}
D:
#include<stdio.h>
#include<vector>
#include<string>
#include<map>
using namespace std;
vector<string> odd_count(vector<string> lst){
    vector<string> output;
    for(int i = 0;i<lst.size();i++){
        int count = 0;
        for(int j=0;j<lst[i].size();j++){
            if(int(lst[i][j])%2 != 0