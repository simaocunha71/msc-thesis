    sort(arr.begin(), arr.end(), [](int a, int b){
        int a_ones = __builtin_popcount(abs(a));
        int b_ones = __builtin_popcount(abs(b));
        if (a_ones == b_ones) {
            return a < b;
        }
        return a_ones < b_ones;
    });
    return arr;
}

int main()
{
    vector<int> arr = {1, 5, 2, 3, 4};
    vector<int> sorted_arr = sort_array(arr);
    for (int i = 0; i < sorted_arr.size(); i++)
        printf("%d ", sorted_arr[i]);
    return 0;
}

This solution uses a lambda function as the third argument to the `std::sort` function. The lambda function compares the number of ones in the binary representation of the absolute values of two integers (using the `__builtin_popcount` function). If the number of ones is the same, it compares the decimal values.

Note that the `abs` function is used to handle negative numbers correctly. This is because the number of ones in the binary representation of a negative number is not defined in the task description.

The `__builtin_popcount` function is a built-in function in GCC that counts the number of ones in a binary representation of a number.
*/

