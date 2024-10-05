    int sum = 0;
    for(int i = 0; i < lst.size(); i++){
        lst[i] = ceil(lst[i]);
        sum += pow(lst[i], 2);
    }
    return sum;
}

int main() {
    vector<float> lst = {1.4, 4.2, 0};
    printf("%d", sum_squares(lst));
    return 0;
}

*/

*/

//C++/SumSquares.cpp
#include<iostream>
#include<math.h>
#include<vector>
using namespace std;
int sum_squares(vector<float> lst){
    int sum = 0;
    for(int i = 0; i < lst.size(); i++){
        lst[i] = ceil(lst[i]);
        sum += pow(lst[i], 2);
    }
    return sum;
}

int main() {
    vector<float> lst = {1.4, 4.2, 0};
    cout<< sum_squares(lst)<<endl;
    return 0;
}

//C++/SumSquaresTest.cpp
#include <gtest/gtest.h>
#include "SumSquares.cpp"

TEST(SumSquaresTest, Test1) {
    vector<float> lst = {1,2,3};
    ASSERT_EQ(sum_squares(lst), 14);
}

TEST(SumSquaresTest, Test2) {
    vector<float> lst = {1,4,9};
    ASSERT_EQ(sum_squares(lst), 98);
}

TEST(SumSquaresTest, Test3) {
    vector<float> lst = {1,3,5,7};
    ASSERT_EQ(sum_squares(lst), 84);
}

TEST(SumSquaresTest, Test4) {
    vector<float> lst = {1.4,4.2,