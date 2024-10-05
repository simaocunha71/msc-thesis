#include<stdio.h>
#include<vector>
using namespace std;

vector<int> even_odd_palindrome(int n){

    vector<int> result;
    for(int i = 1; i <= n; i++){

        if(i % 2 == 0){

            if(i == pow(i, 2))
                result.push_back(1);

        }else{

            if(i == pow(i, 2))
                result.push_back(1);
        }
    }
    int even = 0;
    int odd = 0;
    for(int i = 0; i < result.size(); i++){

        if(result[i] == 1)
            if(i % 2 == 0)
                even++;
            else
                odd++;
    }
    result.push_back(even);
    result.push_back(odd