#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string exchange(vector<int> lst1,vector<int> lst2){
    int count1 = 0;
    for(int i = 0; i < lst1.size(); i++){
        if(lst1[i] % 2 == 0){
            count1++;
        }
    }
    int count2 = 0;
    for(int i = 0; i < lst2.size(); i++){
        if(lst2[i] % 2 == 1){
            count2++;
        }
    }
    if(count1 == lst1.size()){
        return "YES";
    }
    else if(count2 == lst2.size()){
        return "NO";
    }
    else{
        return "YES";
    }
}

B:
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string exchange(vector<int> lst1,vector<int> lst2){
    int count1 = 0;
    for(int i = 0; i < lst1.size(); i++){
        if(lst1[i] % 2 == 0){
            count1++;
        }
    }
    int count2 = 0;
    for(int i = 0; i < lst2.size(); i++){
        if(lst2[i] % 2 == 1){
            count2++;
        }
    }
    if(count1 == lst1.size()){
        return "YES";
    }
    else if(count2 == lst2.size()){
        return "NO";
    }
    else{
        return "YES";
    }
}

C:
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string exchange(vector<int> lst1,vector<int> lst2){
    int count1 = 0;
    for(int i = 0; i < lst1.size(); i++){
        if(lst1[i] % 2 == 0){
            count1++;
        }
    }
    int count2 = 0;
    for(int i = 0; i < lst2.size(); i++){
        if(lst2[i] % 2 == 1){
            count2++;
        }
    }
    if(count1 == lst1.size()){
        return "YES";
    }
    else if(count2 == lst2.size()){
        return "NO";
    }
    else{
        return "YES";
    }
}

D:
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string exchange(vector<int> lst1,vector<int