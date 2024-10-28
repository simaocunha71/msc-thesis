    long long sum = 0, minSum = 0;
    for(int i = 0; i < nums.size(); i++){
        sum += nums[i];
        if(sum < minSum)
            minSum = sum;
    }
    return minSum;
}

int main(){
    vector<long long> nums = {-1, -2, -3};
    printf("%lld\n", minSubArraySum(nums));
    return 0;
}

*/

//src/main.cpp
#include "MinSubArraySum.cpp"

int main(){
    vector<long long> nums = {-1, -2, -3};
    printf("%lld\n", minSubArraySum(nums));
    return 0;
}

//test/MinSubArraySum.spec.cpp
#include <gtest/gtest.h>
#include "../src/MinSubArraySum.cpp"

TEST(MinSubArraySumTest, HandlesEmptyVector) {
    vector<long long> nums = {};
    ASSERT_EQ(minSubArraySum(nums), 0);
}

TEST(MinSubArraySumTest, HandlesNegativeNumbers) {
    vector<long long> nums = {-1, -2, -3};
    ASSERT_EQ(minSubArraySum(nums), -6);
}

TEST(MinSubArraySumTest, HandlesPositiveNumbers) {
    vector<long long> nums = {2, 3, 4, 1, 2, 4};
    ASSERT_EQ(minSubArraySum(nums), 1);
}

TEST(MinSubArraySumTest, HandlesMixedNumbers) {
    vector<long long> nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    ASSERT_EQ(minSubArraySum(nums), -6);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();