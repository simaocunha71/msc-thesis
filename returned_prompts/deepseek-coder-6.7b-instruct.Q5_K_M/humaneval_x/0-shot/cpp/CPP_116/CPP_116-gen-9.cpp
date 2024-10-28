    sort(arr.begin(), arr.end(), [](int a, int b) {
        int a_ones = __builtin_popcount(a);
        int b_ones = __builtin_popcount(b);
        return a_ones < b_ones || (a_ones == b_ones && a < b);
    });
    return arr;
}

int main() {
    vector<int> arr = {1, 5, 2, 3, 4};
    arr = sort_array(arr);
    for(int i=0; i<arr.size(); i++)
        printf("%d ", arr[i]);
    return 0;
}

In the function:
__builtin_popcount(a) is a built-in function in C++, which gives the number of set bits in the binary representation of a number.
*/

// C++ code
#include <iostream>
#include <vector>
#include <algorithm>

std::vector<int> sort_vector(std::vector<int> arr) {
    std::sort(arr.begin(), arr.end(), [](int a, int b) {
        int a_ones = __builtin_popcount(a);
        int b_ones = __builtin_popcount(b);
        return a_ones < b_ones || (a_ones == b_ones && a < b);
    });
    return arr;
}

int main() {
    std::vector<int> arr = {1, 5, 2, 3, 4};
    arr = sort_vector(arr);
    for(int num : arr)
        std::cout << num << " ";
    return 0;
}

The __builtin_popcount function is used to count the number of set bits in the binary representation of an integer. The sort function is then used to sort the vector according to the number of set bits in the binary representation of the integers, and in case of a tie, the decimal values of the integers are used to break the tie.
*/

// C++ code
#include <iostream>
#include <vector>
#include <algorithm>

int