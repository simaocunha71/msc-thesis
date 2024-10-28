    int n = cbrt(a);
    return n * n * n == a;
}

int main() {
    printf("%d\n", iscuber(1));
    printf("%d\n", iscuber(2));
    printf("%d\n", iscuber(-1));
    printf("%d\n", iscuber(64));
    printf("%d\n", iscuber(0));
    printf("%d\n", iscuber(180));

    return 0;
}

*/

//Test/cpp/iscubetest.cpp
#include "iscube.cpp"
#include "gtest/gtest.h"

TEST(iscubeTest, positiveTests){
    EXPECT_TRUE(iscuber(1));
    EXPECT_FALSE(iscuber(2));
    EXPECT_TRUE(iscuber(-1));
    EXPECT_TRUE(iscuber(64));
    EXPECT_TRUE(iscuber(0));
    EXPECT_FALSE(iscuber(180));
}

//Test/cpp/iscubetest.h
#include "iscube.cpp"
#include "gtest/gtest.h"

class iscubeTest : public ::testing::Test {
protected:
    virtual void SetUp() {}
    virtual void TearDown() {}
};

TEST_F(iscubeTest, positiveTests){
    EXPECT_TRUE(iscuber(1));
    EXPECT_FALSE(iscuber(2));
    EXPECT_TRUE(iscuber(-1));
    EXPECT_TRUE(iscuber(64));
    EXPECT_TRUE(iscuber(0));
    EXPECT_FALSE(iscuber(180));
}

//Test/cpp/main.cpp
#include "gtest/gtest.h"
#include "iscubetest.h"

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

//Test/cpp/main_iscube.cpp
#include "iscube.cpp"
#include <iostream>

int main() {
   