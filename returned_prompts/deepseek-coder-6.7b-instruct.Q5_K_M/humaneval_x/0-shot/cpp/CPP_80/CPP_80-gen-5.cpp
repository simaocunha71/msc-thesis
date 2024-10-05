    if (s.length()<3){
        return false;
    }
    else{
        for(int i=0; i<s.length()-2; i++){
            if (s[i] == s[i+1] || s[i+1] == s[i+2] || s[i] == s[i+2]){
                return false;
            }
        }
    }
    return true;
}
int main(){
    string s;
    printf("Enter a string: ");
    getline(cin, s);
    if(is_happy(s)){
        printf("The string is happy\n");
    }else{
        printf("The string is not happy\n");
    }
    return 0;
}

//tests/test_happy.cpp
#include <gtest/gtest.h>
#include <string>
#include "../src/happy.cpp"

TEST(happyTest, test1){
    EXPECT_FALSE(is_happy("a"));
}

TEST(happyTest, test2){
    EXPECT_FALSE(is_happy("aa"));
}

TEST(happyTest, test3){
    EXPECT_TRUE(is_happy("abcd"));
}

TEST(happyTest, test4){
    EXPECT_FALSE(is_happy("aabb"));
}

TEST(happyTest, test5){
    EXPECT_TRUE(is_happy("adb"));
}

TEST(happyTest, test6){
    EXPECT_FALSE(is_happy("xyy"));
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}