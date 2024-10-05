
}

int main(){
    vector<int> arr = {2, 1, 1, 4, 5, 8, 2, 3};
    vector<string> result = by_length(arr);
    for (int i=0; i<result.size(); i++)
       printf("%s ", result[i].c_str());
    return 0;
}

*/

//main.cpp
#include<stdio.h>
#include<vector>
#include<string>
#include<map>
#include<algorithm>
using namespace std;

vector<string> by_length(vector<int> arr){
    vector<string> result;
    map<int, string> num_to_name = {{1, "One"}, {2, "Two"}, {3, "Three"}, {4, "Four"}, {5, "Five"}, {6, "Six"}, {7, "Seven"}, {8, "Eight"}, {9, "Nine"}};

    for(int num: arr){
        if(num >= 1 && num <= 9){
            result.push_back(num_to_name[num]);
        }
    }
    sort(result.begin(), result.end());
    reverse(result.begin(), result.end());
    return result;
}

int main(){
    vector<int> arr = {2, 1, 1, 4, 5, 8, 2, 3};
    vector<string> result = by_length(arr);
    for (int i=0; i<result.size(); i++)
       printf("%s ", result[i].c_str());
    return 0;
}

//main_test.cpp
#include "main.cpp"
#include "gtest/gtest.h"

TEST(by_length, by_lengthTest) {
    EXPECT_EQ(by_length({2, 1, 1, 4, 5, 8, 2, 3}), {"Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"});
    EXPECT_EQ