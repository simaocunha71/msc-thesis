    vector<int> result;
    for (int i = 0; i < x.size(); i++) {
        int num = x[i];
        bool has_even_digit = false;
        while (num > 0) {
            int digit = num % 10;
            if (digit % 2 == 0) {
                has_even_digit = true;
                break;
            }
            num /= 10;
        }
        if (!has_even_digit) {
            result.push_back(x[i]);
        }
    }
    sort(result.begin(), result.end());
    return result;
}
// Another solution
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> unique_digits(vector<int> x){
    vector<int> result;
    for(int i=0; i<x.size(); i++){
        int num=x[i];
        bool has_even_digit=false;
        while(num>0){
            int digit=num%10;
            if(digit%2==0){
                has_even_digit=true;
                break;
            }
            num=num/10;
        }
        if(!has_even_digit){
            result.push_back(x[i]);
        }
    }
    sort(result.begin(), result.end());
    return result;
}
// Yet another solution
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> unique_digits(vector<int> x){
    vector<int> result;
    for(int i=0; i<x.size(); i++){
        int num=x[i];
        bool has_even_digit=false;
        while(num>0){
            int digit=num%10;
            if(digit%2==0){
                has_even_digit=true;
                break;
            }
            num=num/10;
        }
        if(!has_even_digit){
            result.push_back(x[i]);
        }
    }
    sort(result.begin(), result.end());
    return result;
}