#include<stdio.h>
#include<math.h>
#include<string>
#include<vector>
using namespace std;
int total_match(vector<string> lst1,vector<string> lst2){
    int sum1=0,sum2=0;
    for(int i=0;i<lst1.size();i++){
        for(int j=0;j<lst1[i].length();j++){
            sum1+=lst1[i][j];
        }
    }
    for(int i=0;i<lst2.size();i++){
        for(int j=0;j<lst2[i].length();j++){
            sum2+=lst2[i][j];
        }
    }
    if(sum1==sum2){
        return 1;
    }
    if(sum1>sum2){
        return 2;
    }
    if(sum1<sum2){
        return 3;
    }
}

