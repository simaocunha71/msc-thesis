    int count = 0;
    size_t found = str.find(substring);
    while (found != string::npos){
        count++;
        found = str.find(substring, found+1);
    }
    return count;
}

int main() {
    printf("%d\n", how_many_times("", "a"));
    printf("%d\n", how_many_times("aaa", "a"));
    printf("%d\n", how_many_times("aaaa", "aa"));
    return 0;
}

*/

*/

//Task 2/main.cpp
#include <iostream>
#include <string>
#include "how_many_times.h"
using namespace std;

int main() {
    cout << how_many_times("", "a") << endl;
    cout << how_many_times("aaa", "a") << endl;
    cout << how_many_times("aaaa", "aa") << endl;
    return 0;
}

//Task 2/test.cpp
#include <gtest/gtest.h>
#include "how_many_times.h"

TEST(how_many_timesTest, returnsCorrectCount) {
    EXPECT_EQ(3, how_many_times("aaa", "a"));
    EXPECT_EQ(2, how_many_times("abcabc", "ab"));
    EXPECT_EQ(0, how_many_times("abcabc", "xyz"));
    EXPECT_EQ(1, how_many_times("aaaaaa", "aaa"));
}

TEST(how_many_timesTest, returnsZeroForEmptySubstring) {
    EXPECT_EQ(0, how_many_times("abc", ""));
    EXPECT_EQ(3, how_many_times("abcabc", ""));
    EXPECT_EQ(0, how_many_times("", ""));
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

//Task 3/main