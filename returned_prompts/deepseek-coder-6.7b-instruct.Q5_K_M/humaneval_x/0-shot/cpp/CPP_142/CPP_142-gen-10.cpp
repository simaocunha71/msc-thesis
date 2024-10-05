    int sum=0;
    for (int i=0;i<lst.size();i++){
        if(i%3==0){
            sum+=lst[i]*lst[i];
        }
        else if(i%4==0){
            sum+=lst[i]*lst[i]*lst[i];
        }
        else{
            sum+=lst[i];
        }
    }
    return sum;
}

int main(){
    vector<int> lst={-1,-5,2,-1,-5};
    printf("%d\n",sum_squares(lst));
    return 0;
}

*/

//Program Ends Here.

*/

//src/main.cpp
#include<iostream>
#include<vector>
#include"functions.h"
using namespace std;

int main(){
    vector<int> lst={1,2,3};
    cout<<sum_squares(lst)<<endl;
    return 0;
}

//src/test.cpp
#include<gtest/gtest.h>
#include<vector>
#include "functions.h"

TEST(SumSquaresTest, PositiveTest){
    vector<int> lst={1,2,3};
    EXPECT_EQ(sum_squares(lst),6);
}

TEST(SumSquaresTest, NegativeTest){
    vector<int> lst={-1,-5,2,-1,-5};
    EXPECT_EQ(sum_squares(lst),-126);
}

TEST(SumSquaresTest, EmptyTest){
    vector<int> lst;
    EXPECT_EQ(sum_squares(lst),0);
}

int main(int argc, char **argv){
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

//include/functions.cpp
#include<iostream>
#include<vector>
#include "functions.h"
using namespace