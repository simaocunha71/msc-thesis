
}

int main() {
    printf("%d\n", prime_length("Hello")); // should be 1
    printf("%d\n", prime_length("abcdcba")); // should be 1
    printf("%d\n", prime_length("kittens")); // should be 1
    printf("%d\n", prime_length("orange")); // should be 0
    return 0;
}

*/

#include <cmath>
bool prime_length(string str) {
    int len = str.length();
    if(len < 2) return false;
    for(int i = 2; i <= sqrt(len); i++) {
        if(len % i == 0) return false;
    }
    return true;
}

//test.cpp
#include "prime_length.cpp"
#include <gtest/gtest.h>

TEST(PrimeLengthTest, HandlesTrueCases) {
    EXPECT_TRUE(prime_length("Hello"));
    EXPECT_TRUE(prime_length("abcdcba"));
    EXPECT_TRUE(prime_length("kittens"));
}

TEST(PrimeLengthTest, HandlesFalseCases) {
    EXPECT_FALSE(prime_length("orange"));
    EXPECT_FALSE(prime_length(""));
    EXPECT_FALSE(prime_length("nonprime"));
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}