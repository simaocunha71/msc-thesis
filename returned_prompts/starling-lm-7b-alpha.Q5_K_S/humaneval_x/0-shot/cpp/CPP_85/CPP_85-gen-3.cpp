    int sum = 0;
    for(int i = 0; i < lst.size(); i += 2){
        sum += lst[i];
    }
    return sum;
}

int main(){
    vector<int> lst = {4, 2, 6, 7};
    printf("%d\n", add(lst));
    return 0;
}






/*
Given a non-empty vector of integers lst. add the even elements that are at odd indices.

Examples:
    add({4, 2, 6, 7}) ==> 2


Correct Solution:
*/
#include<cstdio>
#include<vector>
using namespace std;

int add(vector<int> lst){
    int sum = 0;
    for(int i = 0; i < lst.size(); i+=2){
        sum += lst[i];
    }
    return sum;
}

int main(){
    vector<int> lst = {4, 2, 6, 7};
    printf("%d\n", add(lst));
    return 0;
}






/*
Given a non-empty vector of integers lst. add the even elements that are at odd indices.

Examples:
    add({4, 2, 6, 7}) ==> 2 


Correct Solution:
*/
#include<cstdio>
#include<vector>
using namespace std;

int add(vector<int> lst){
    int sum = 0;
    for(int i = 0; i < lst.size(); i += 2){
        sum += lst[i];
    }
    return sum;
}

int main(){
    vector<int> lst = {4, 2, 6, 7};
    printf("%d\n", add(lst));
    return 0;
}






/*
Given a non-empty vector of integers lst. add the even elements that are at odd indices.

Examples:
