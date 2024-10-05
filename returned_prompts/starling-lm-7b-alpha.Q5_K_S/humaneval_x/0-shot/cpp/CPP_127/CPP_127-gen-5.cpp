    if(interval2[0]>interval1[1]){
        return "NO";
    }
    else if(interval1[0]>interval2[1]){
        return "NO";
    }
    else if(interval2[0]>interval1[0]){
        if(interval2[0]>interval1[1]){
            return "NO";
        }
        else if(interval1[1]>interval2[1]){
            return "NO";
        }
        else if(interval2[0]<=interval1[0] && interval2[1]>=interval1[1]){
            return "YES";
        }
    }
    else if(interval2[0]<=interval1[0] && interval2[1]>=interval1[1]){
        return "YES";
    }
    else if(interval1[0]>interval2[0] && interval1[1]<interval2[1]){
        return "YES";
    }

    return "NO";
}

int main(){
    vector<int> interval1;
    interval1.push_back(-3);
    interval1.push_back(-1);
    vector<int> interval2;
    interval2.push_back(-5);
    interval2.push_back(5);
    printf("%s\n",intersection(interval1,interval2).c_str());
    return 0;
}



























































*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string intersection( vector<int> interval1,vector<int> interval2){

    if(interval2[0]>interval1[1]){
        return "NO";
    }
    else if(interval1[0]>interval2[1]){
        return "NO";
    }
    else if(interval2[0]>interval1