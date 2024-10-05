    int count = 0;

B:
    for(int i = 0; i < nums.size(); i++){
        if(nums[i] > 10){
            int lastDigit = abs(nums[i] % 10);
            int firstDigit = abs((nums[i] / 10) % 10);
            if(lastDigit % 2 != 0 && firstDigit % 2 != 0){
                count++;
            }
        }
    }

C:
    return count;
}

int main(){
    vector<int> nums1 = {15, -73, 14, -15};
    printf("%d\n", specialFilter(nums1)); // Output: 1
    vector<int> nums2 = {33, -2, -3, 45, 21, 109};
    printf("%d\n", specialFilter(nums2)); // Output: 2
    return 0;
}
*/

// Write your C++ code here
#include<vector>
#include<cmath>
using namespace std;

int specialFilter(vector<int> nums){
    int count = 0;
    for(int i = 0; i < nums.size(); i++){
        if(nums[i] > 10){
            int lastDigit = abs(nums[i] % 10);
            int firstDigit = abs((nums[i] / 10) % 10);
            if(lastDigit % 2 != 0 && firstDigit % 2 != 0){
                count++;
            }
        }
    }
    return count;
}

//test/main.cpp
#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "doctest.h"
#include "../src/main.cpp"

TEST_CASE("testing specialFilter function") {
    // Testing the first example in the problem
    vector<int> nums1 = {15, -73, 14, -15};
   