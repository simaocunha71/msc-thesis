#include<stdio.h>
#include<vector>
using namespace std;
vector<int> generate_integers(int a,int b){
    vector<int> result;
    while(a<=b){
        int temp=a;
        while(temp){
            int digit=temp%10;
            if(digit%2==0){
                result.push_back(digit);
            }
            temp/=10;
        }
        a++;
    }
    return result;
}
