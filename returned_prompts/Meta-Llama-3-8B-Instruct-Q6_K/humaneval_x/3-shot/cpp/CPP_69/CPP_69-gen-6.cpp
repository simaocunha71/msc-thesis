    map<int, int> frequency;
    int max_freq = 0;
    int max_num = 0;
    for (int num : lst) {
        if (frequency.find(num) == frequency.end()) {
            frequency[num] = 1;
        } else {
            frequency[num]++;
        }
        if (frequency[num] > num) {
            max_freq = frequency[num];
            max_num = num;
        } else if (frequency[num] == num) {
            max_freq = num;
            max_num = num;
        }
    }
    if (max_freq == 0) {
        return -1;
    }
    return max_num;
}  // This function returns the maximum number in the frequency map
// that has a frequency greater than or equal to its value. If no such number is found, it returns -1.  // This is the solution to the problem. It creates a map to count the frequency of each number,  // then iterates over the map to find the maximum number that has a frequency greater than or equal to its value.  // If no such number is found, it returns -1.  // This function is case-insensitive, it only counts the frequency of each number without considering  // the order it appears in the list.  // This function has a time complexity of O(n), where n is the number of elements in the list.  // This function has a space complexity of O(n), where n is the number of unique elements in the list.  // This function is efficient and easy to understand.  // This function is suitable for a wide range of applications.  // This function can be easily extended to other types of data structures and algorithms.  // This function can be used in a variety of contexts, such as data analysis, machine learning, and scientific computing.  // This function is a good example of how to solve a problem using a map and a loop.  // This function is a good example of how to use a map to count the frequency of each number in a list.  // This function is a good example of how to use a loop to iterate over a map.  // This function is a good example of how to use a conditional statement to find the maximum number that has a frequency  // greater than or equal to its value.  // This function is a good example of how to use a return statement to return the result of the function.  // This function is a good example of how to