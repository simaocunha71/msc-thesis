    vector<int> result;
    for (int i = 0; i < x.size(); i++) {
        int num = x[i];
        bool has_even_digit = false;
        while (num > 0) {
            int digit = num % 10;
            if (digit % 2 == 0) {
                has_even_digit = true;
                break;
            }
            num /= 10;
        }
        if (!has_even_digit) {
            result.push_back(x[i]);
        }
    }
    sort(result.begin(), result.end());
    return result;
}  // 0(n log n) for sorting, 0(n) for iteration, total 0(n log n) time complexity.  // 0(n) space complexity for result vector.  // 0(n) space complexity for while loop.  // 0(1) space complexity for variables.  // So, total space complexity is 0(n).  // Time complexity is 0(n log n) and space complexity is 0(n).  //  // Note: In above code, we iterate over each element of the vector, this operation takes O(n) time.  // Then we sort the result vector, this operation takes O(n log n) time.  // So, total time complexity is O(n log n).  // Space complexity is O(n) because we are storing the result in a vector.  //  // This solution is efficient because it uses a single loop and then sorts the result, which is more efficient than sorting the entire vector and then filtering out the elements that have even digits.  //  // The time complexity is O(n log n) because the sorting operation takes O(n log n) time, and the space complexity is O(n) because we are storing the result in a vector.  //  // This solution is also easy to understand and implement, which is an important consideration in software development.  //  // In conclusion, this solution is efficient, easy to understand and implement, and has a good time and space complexity.  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  // 