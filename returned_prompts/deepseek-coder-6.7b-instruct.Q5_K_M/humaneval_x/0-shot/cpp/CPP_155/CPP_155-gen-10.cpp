    vector<int> ans(2, 0);
    num = abs(num);
    while(num > 0){
        if((num % 10) % 2 == 0)
            ans[0]++;
        else
            ans[1]++;
        num /= 10;
    }
    return ans;
}

int main(){
    int num;
    scanf("%d", &num);
    vector<int> ans = even_odd_count(num);
    printf("Even count: %d\nOdd count: %d\n", ans[0], ans[1]);
    return 0;
}
*/

//CPP/Test/test.cpp
#include "gtest/gtest.h"
#include "../Source/main.cpp"

TEST(EvenOddCountTest, PositiveNumberTest) {
    EXPECT_EQ(even_odd_count(123), (vector<int>{1, 2}));
    EXPECT_EQ(even_odd_count(113355), (vector<int>{3, 3}));
    EXPECT_EQ(even_odd_count(2468), (vector<int>{4, 0}));
}

TEST(EvenOddCountTest, NegativeNumberTest) {
    EXPECT_EQ(even_odd_count(-123), (vector<int>{1, 2}));
    EXPECT_EQ(even_odd_count(-113355), (vector<int>{3, 3}));
    EXPECT_EQ(even_odd_count(-2468), (vector<int>{4, 0}));
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}/*
