
The function `is_multiply_prime()` will check if a number is a product of exactly three different prime numbers. The given number is passed as an argument `a` to the function. Inside the function, a for loop is used to check each number from 2 to `a` (inclusive). If `a` is divisible by the number `i` (no remainder), a while loop is used to keep dividing `a` by `i` until `a` can no longer be divided by `i`. The count of such prime factors is incremented by 1 for each prime factor found. If the count is exactly 3, the function returns `true`, else it returns `false`. The `main()` function then calls this function with `30` as the argument and prints the result.
*/

// @lc code=end

// @lc code=start
/*
// @lc app=leetcode id=1512 lang=cpp
//
// [1512] Number of Good Pairs
//
// 