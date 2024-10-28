    int changes = 0, i = 0, j = arr.size() - 1;
    while (i < j)
    {
        if (arr[i] != arr[j])
            changes++;
        i++;
        j--;
    }
    return changes;
}

int main(){
    vector<int> arr = {1,2,3,5,4,7,9,6};
    printf("%d\n", smallest_change(arr)); // 4
    vector<int> arr2 = {1, 2, 3, 4, 3, 2, 2};
    printf("%d\n", smallest_change(arr2)); // 1
    vector<int> arr3 = {1, 2, 3, 2, 1};
    printf("%d\n", smallest_change(arr3)); // 0
    return 0;
}

*/

#include <vector>
using namespace std;

int smallest_change(vector<int> arr) {
    int changes = 0, i = 0, j = arr.size() - 1;
    while (i < j)
    {
        if (arr[i] != arr[j])
            changes++;
        i++;
        j--;
    }
    return changes;
}

//tests/test_smallest_change.cpp
#define CATCH_CONFIG_MAIN
#include "catch.hpp"
#include "smallest_change.cpp"

TEST_CASE("Smallest change") {
    REQUIRE(smallest_change(vector<int>{1,2,3,5,4,7,9,6}) == 4);
    REQUIRE(smallest_change(vector<int>{1, 2, 3, 4, 3, 2, 2}) == 1);
    REQUIRE(smallest_change(vector<int>{1, 2, 3, 2, 1}) == 0);
}

//tests/test_smallest_change_main.cpp
#include <iostream>
#include <vector>
#include "small