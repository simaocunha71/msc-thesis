  int n = text.length();

  for(int i=0; i<n/2; i++)
    if (text[i] != text[n-i-1])
      return false;

  return true;
}

int main(){
  printf("%d", is_palindrome("aba"));
  return 0;
}

*/

int main() {
    cout << boolalpha << is_palindrome("") << endl;
    cout << boolalpha << is_palindrome("aba") << endl;
    cout << boolalpha << is_palindrome("aaaaa") << endl;
    cout << boolalpha << is_palindrome("zbcd") << endl;
    return 0;
}

//src/main.cpp
#include <iostream>
#include <cctype>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

// Question
// Given an array of integers, find the length of the longest increasing subsequence.

// Solution
// Dynamic Programming

int lengthOfLIS(vector<int>& nums) {
    int n = nums.size();
    if (n == 0) return 0;
    vector<int> dp(n, 1);
    int max_length = 1;
    for (int i = 1; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (nums[i] > nums[j]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
        max_length = max(max_length, dp[i]);
    }
    return max_length;
}

int main() {
    vector<int> nums = {10, 9, 2, 5, 3, 7, 101, 18};
    cout << lengthOfLIS(nums) << endl;
    return 0;
}

//src/main_1.cpp
#include <