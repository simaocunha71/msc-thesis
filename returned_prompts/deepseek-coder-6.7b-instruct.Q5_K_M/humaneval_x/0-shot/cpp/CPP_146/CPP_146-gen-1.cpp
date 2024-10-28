
}

int main(){
    vector<int> nums = {15, -73, 14, -15};
    printf("%d", specialFilter(nums));

    return 0;
}

*/

#include<bits/stdc++.h>
using namespace std;

bool isValid(int num) {
    if(num < 0) num *= -1;
    string s = to_string(num);
    int first = s[0] - '0';
    int last = s[s.size() - 1] - '0';
    return (num > 10 && (first % 2 == 1) && (last % 2 == 1));
}

int specialFilter(vector<int> nums){
    int count = 0;
    for(int i = 0; i < nums.size(); i++) {
        if(isValid(nums[i])) count++;
    }
    return count;
}

int main(){
    vector<int> nums = {15, -73, 14, -15};
    printf("%d", specialFilter(nums));

    return 0;
}

//src/c++/problems/specialFilter.cpp
/*
