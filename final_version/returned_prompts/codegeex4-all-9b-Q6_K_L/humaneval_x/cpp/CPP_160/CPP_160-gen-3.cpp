```cpp
#include<stdio.h>
#include<math.h>
#include<vector>
#include<string>
using namespace std;
#include<algorithm>
#include<stdlib.h>

int do_algebra(vector<string> operato, vector<int> operand){

    int result=0;
    for(int i=0;i<operato.size();i++){
        if(operato[i]=="+"){
            result+=operand[i];
        }
        else if(operato[i]=="-"){
            result-=operand[i];
        }
        else if(operato[i]=="*"){
