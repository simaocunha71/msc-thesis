    int min_val = arr[0];
    int min_index = 0;
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] % 2 == 0 && arr[i] < min_val) {
            min_val = arr[i];
            min_index = i;
        }
    }
    if (min_val == 0) {
        return {min_val, min_index};
    }
    while(min_index < arr.size() && arr[min_index] % 2 == 0) {
        if (arr[min_index+1] % 2 == 0 && arr[min_index+1] < min_val) {
            min_val = arr[min_index+1];
            min_index++;
        } else {
            break;
        }
    }
    return {min_val, min_index};
}


int main() {
    vector<int> arr = {4,2,3};
    vector<int> res = pluck(arr);
    printf("%d %d\n", res[0], res[1]);
    return 0;
}
*/


/*
Given a string s consisting of lowercase English letters, return the number of unique characters in the string.

For example, if you are given a string "abcde", the unique characters are 'a', 'b', 'c', 'd', 'e'. The number of unique characters is 5.

Example 1:
Input: "abc"
Output: 3
Explanation: The unique characters are 'a', 'b', and 'c'.

Example 2:
Input: "abcdefghijklmnopqrstuvwxyz"
Output: 26

Constraints:
1 <= s.length <= 10^6

Solution:
The simplest way to solve this problem is to create a set and add all the unique characters from the string to it.
The size of the set will be equal to the number of unique characters in the string.

Here's a step-by-step guide:

Create a set to store the unique