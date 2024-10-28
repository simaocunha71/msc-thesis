    vector<int> result;
    if(a>b)
    {
        int temp=a;
        a=b;
        b=temp;
    }
    for(int i=a; i<=b; i++)
    {
        if(i%2==0)
        {
            result.push_back(i);
        }
    }
    return result;
}

int main()
{
    vector<int> result = generate_integers(2, 8);
    for(int i=0; i<result.size(); i++)
    {
        printf("%d ", result[i]);
    }
    return 0;
}

*/

int main()
{
    vector<int> result = generate_integers(2, 8);
    for(int i=0; i<result.size(); i++)
    {
        printf("%d ", result[i]);
    }
    return 0;
}

//C++/generate_integers_test.cpp
#include "generate_integers.cpp"
#include<gtest/gtest.h>

TEST(GenerateIntegers, Test1){
    vector<int> res = generate_integers(2,8);
    vector<int> exp = {2, 4, 6, 8};
    ASSERT_EQ(res, exp);
}

TEST(GenerateIntegers, Test2){
    vector<int> res = generate_integers(8,2);
    vector<int> exp = {2, 4, 6, 8};
    ASSERT_EQ(res, exp);
}

TEST(GenerateIntegers, Test3){
    vector<int> res = generate_integers(10,14);
    vector<int> exp = {};
    ASSERT_EQ(res, exp);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

//C++/generate_integers_test_v2.cpp
#include "generate_integers