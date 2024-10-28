    int count=0;
    bool flag=false;
    for(int i=0;i<S.size();i++){
        if(S[i]=='I' && i+1<S.size() && (S[i+1]==' ' || S[i+1]=='.' || S[i+1]=='?' || S[i+1]=='!')){
            count++;
            flag=true;
        }
        else if(S[i]=='.' || S[i]=='?' || S[i]=='!' ){
            flag=false;
        }
    }
    if(flag)
        count++;
    return count;
}

int main(){
    printf("%d\n",is_bored("Hello world")); // output: 0
    printf("%d\n",is_bored("The sky is blue. The sun is shining. I love this weather")); // output: 1
    return 0;
}

*/

/*

*/

// End of Source Code

// CPP_Programs/C++/Test_Cases_for_is_bored.cpp
#include "is_bored.cpp"
#include <gtest/gtest.h>

TEST(is_boredTest, case1) {
    EXPECT_EQ(0, is_bored("Hello world"));
}

TEST(is_boredTest, case2) {
    EXPECT_EQ(1, is_bored("The sky is blue. The sun is shining. I love this weather"));
}

TEST(is_boredTest, case3) {
    EXPECT_EQ(2, is_bored("I am bored. You are bored. We are all bored."));
}

TEST(is_boredTest, case4) {
    EXPECT_EQ(1, is_bored("I am bored? Yes, I am. We are all bored."));
}

TEST(is_boredTest, case5) {
    EXPECT_EQ(1, is_bored("I am bored. Are you bored too?"));
}

int main(int argc, char **