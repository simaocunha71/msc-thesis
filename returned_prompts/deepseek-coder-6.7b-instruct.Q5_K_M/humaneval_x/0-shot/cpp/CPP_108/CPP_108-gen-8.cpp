    int sum = 0;
    for(int i=0; i<n.size(); i++){
        if(n[i]<0){
            int num = n[i];
            while(num){
                sum += num%10;
                num /= 10;
            }
        }
        else{
            int num = n[i];
            while(num){
                sum += num%10;
                num /= 10;
            }
        }
        if(sum > 0)
            return i+1;
    }
    return 0;
}

*/

*/

#include <iostream>
#include<vector>
#include "count_nums.h"
using namespace std;

int main(){
    vector<int> n = {-1, 11, -11};
    cout<<count_nums(n);
    return 0;
}

//test/test_count_nums.cpp
#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"
#include "count_nums.h"
#include<vector>
using namespace std;

TEST_CASE("Testing count_nums function"){
    SECTION("Test 1"){
        vector<int> n = {};
        REQUIRE(count_nums(n) == 0);
    }
    SECTION("Test 2"){
        vector<int> n = {-1, 11, -11};
        REQUIRE(count_nums(n) == 1);
    }
    SECTION("Test 3"){
        vector<int> n = {1, 1, 2};
        REQUIRE(count_nums(n) == 3);
    }
}