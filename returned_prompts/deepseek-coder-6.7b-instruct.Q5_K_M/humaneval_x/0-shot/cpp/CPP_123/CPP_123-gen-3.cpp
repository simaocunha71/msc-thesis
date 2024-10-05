    vector<int> odd_numbers;
    while(n != 1){
        if(n % 2 != 0){
            odd_numbers.push_back(n);
        }
        n = n % 2 ? n*3 + 1 : n / 2;
    }
    odd_numbers.push_back(1);
    sort(odd_numbers.begin(), odd_numbers.end());
    return odd_numbers;
}

int main(){
    int n;
    printf("Enter a positive integer: ");
    scanf("%d",&n);
    vector<int> odd_numbers = get_odd_collatz(n);
    printf("The odd numbers in the Collatz sequence are: ");
    for(int i=0; i<odd_numbers.size(); i++){
        printf("%d ",odd_numbers[i]);
    }
    printf("\n");
    return 0;
}
// The time complexity of the solution is O(n log n) due to the sorting operation.
// The space complexity of the solution is O(n), as we are storing the odd numbers in a vector.

*/

//C++/HW5/test.cpp
#include "gtest/gtest.h"
#include "HW5.cpp"

TEST(GetOddCollatzTest, PositiveNumbers) {
    EXPECT_EQ(get_odd_collatz(1), std::vector<int>({1}));
    EXPECT_EQ(get_odd_collatz(5), std::vector<int>({1, 5}));
    EXPECT_EQ(get_odd_collatz(10), std::vector<int>({1, 5, 11, 27}));
    EXPECT_EQ(get_odd_collatz(15), std::vector<int>({1, 5, 11, 17, 25, 45, 61}));
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_