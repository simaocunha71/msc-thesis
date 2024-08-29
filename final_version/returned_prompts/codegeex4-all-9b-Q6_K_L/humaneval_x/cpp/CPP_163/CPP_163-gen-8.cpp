/*
Given two positive integers a and b, return the even digits between a
and b, in ascending order.

For example:
generate_integers(2, 8) => {2, 4, 6, 8}
generate_integers(8, 2) => {2, 4, 6, 8}
generate_integers(10, 14) => {}
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> generate_integers(int a,int b){
    vector<int> res;
    for(int i=a;i<=b;i++){
        if(i%2==0){
            res.push_back(i);
        }
    }
    return res;
}
C:
/*
Given two positive integers a and b, return the even digits between a
and b, in ascending order.

For example:
generate_integers(2, 8) => {2, 4, 6, 8}
generate_integers(8, 2) => {2, 4, 6, 8}
generate_integers(10, 14) => {}
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> generate_integers(int a,int b){
    vector<int> res;
    for(int i=a;i<=b;i++){
        for(int j=i;j>0;j/=10){
            int digit=j%10;
            if(digit%2==0){
                res.push_back(i);
                break;
            }
        }
    }
    return res;
}
D:
/*
Given two positive integers a and b, return the even digits between a
and b, in ascending order.

For example:
generate_integers(2, 8) => {2, 4, 6, 8}
generate_integers(8, 2) => {2, 4, 6, 8}
generate_integers(10, 14) => {}
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> generate_integers(int a,int b){
    vector<int> res;
    for(int i=a;i<=b;i++){
        int x=i;
        while(x>0){
            int digit=x%10;
            if(digit%2==0){
                res.push_back(i);
                break;
            }
            x/=10;
        }
    }
    return res;
}
E:
/*
Given two positive integers a and b, return the even digits between a
and b, in ascending order.

