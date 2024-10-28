This algorithm works by comparing the elements from the ends of the array towards the center. If the elements are not equal, it increments a counter. Since a palindrome vector is a vector that is the same read backwards and forwards, the elements need to be equal at the corresponding positions from both ends. Therefore, the counter gives the minimum number of changes required to make the vector palindromic.

The time complexity of this algorithm is O(n), where n is the size of the array. This is because the algorithm has to traverse half of the array to compare elements from both ends. The space complexity is O(1), as no additional space is used that scales with the size of the input.

In the given example, the vector {1, 2, 3, 2, 1} is already a palindrome, so the function returns 0, as no elements need to be changed.
*/

#endif // __MINIMUM_CHANGE_TO_MAKE_VECTOR_PALINDROMIC_H__

//src/main.cpp
#include <iostream>
#include <vector>
#include "minimum_change_to_make_vector_palindromic.h"

int main() {
    std::vector<int> arr = {1, 2, 3, 2, 1};
    std::cout << smallest_change(arr) << std::endl;
    return 0;
}

//test/test_minimum_change_to_make_vector_palindromic.cpp
#include "gtest/gtest.h"
#include "minimum_change_to_make_vector_palindromic.h