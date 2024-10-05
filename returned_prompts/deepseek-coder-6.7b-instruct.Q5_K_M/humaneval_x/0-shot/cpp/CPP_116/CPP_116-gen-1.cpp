sort(arr.begin(), arr.end(), [](int a, int b){
    int count_a = __builtin_popcount(abs(a));
    int count_b = __builtin_popcount(abs(b));

    if (count_a == count_b)
        return a < b;
    else
        return count_a < count_b;});

return arr;
}
*/

*/

#include <vector>
#include <algorithm>
#include <cstdlib>

std::vector<int> sort_vector(std::vector<int> arr) {
    std::sort(arr.begin(), arr.end(), [](int a, int b) {
        int count_a = __builtin_popcount(abs(a));
        int count_b = __builtin_popcount(abs(b));

        if (count_a == count_b)
            return a < b;
        else
            return count_a < count_b;
    });

    return arr;
}

// #include <iostream>
// int main() {
//     auto sorted = sort_vector({1, 5, 2, 3, 4});
//     for (auto i : sorted) {
//         std::cout << i << " ";
//     }
//     std::cout << std::endl;

//     return 0;
// }

//src/main.cpp
#include <iostream>
#include "kata.cpp"

int main() {
    auto sorted = sort_vector({1, 5, 2, 3, 4});
    for (auto i : sorted) {
        std::cout << i << " ";
    }
    std::cout << std::endl;

    return 0;
}

//test/test.cpp
#define CATCH_CONFIG_MAIN
#include "catch.hpp"
#include "../src/kata.cpp"

TEST_CASE("Sorting vector with positive integers", "[sort_vector]") {
    REQUIRE(sort_vector({1, 5, 