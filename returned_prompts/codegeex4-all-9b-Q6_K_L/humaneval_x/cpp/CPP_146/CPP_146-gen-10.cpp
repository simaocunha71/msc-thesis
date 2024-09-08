#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int specialFilter(vector<int> nums){
    int count = 0;
    for(int i = 0; i < nums.size(); i++){
        if(nums[i] > 10 && nums[i] % 2 != 0){
            int lastDigit = nums[i] % 10;
            int firstDigit = nums[i] / pow(10, int(log10(nums[i])));
            if(lastDigit % 2 != 0 && firstDigit % 2 != 0){
                count++;
            }
        }
    }
    return count;
}

B:
#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int specialFilter(vector<int> nums){
    int count = 0;
    for(int i = 0; i < nums.size(); i++){
        if(nums[i] > 10 && nums[i] % 2 != 0){
            int lastDigit = nums[i] % 10;
            int firstDigit = nums[i] / pow(10, int(log10(nums[i])));
            if(lastDigit % 2 != 0 && firstDigit % 2 != 0){
                count++;
            }
        }
    }
    return count;
}

C:
#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int specialFilter(vector<int> nums){
    int count = 0;
    for(int i = 0; i < nums.size(); i++){
        if(nums[i] > 10 && nums[i] % 2 != 0){
            int lastDigit = nums[i] % 10;
            int firstDigit = nums[i] / pow(10, int(log10(nums[i])));
            if(lastDigit % 2 != 0 && firstDigit % 2 != 0){
                count++;
            }
        }
    }
    return count;
}

D:
#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int specialFilter(vector<int> nums){
    int count = 0;
    for(int i = 0; i < nums.size(); i++){
        if(nums[i] > 10 && nums[i] % 2 != 0){
            int lastDigit = nums[i] % 10;
            int firstDigit = nums[i] / pow(10, int(log10(nums[i])));
            if(lastDigit % 2 != 0 && firstDigit % 2 != 0){
                count++;
           