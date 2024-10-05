  map<int, string> num_to_str = {{1, "One"}, {2, "Two"}, {3, "Three"}, {4, "Four"}, {5, "Five"}, {6, "Six"}, {7, "Seven"}, {8, "Eight"}, {9, "Nine"}};
  vector<string> result;
  vector<int> valid_nums;
  for(auto num : arr)
    if(num>=1 && num<=9)
      valid_nums.push_back(num);
  sort(valid_nums.begin(), valid_nums.end());
  reverse(valid_nums.begin(), valid_nums.end());
  for(auto num : valid_nums)
    result.push_back(num_to_str[num]);
  return result;
}
*/

// Test Cases:
// Input: {2, 1, 1, 4, 5, 8, 2, 3}
// Output: {"Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"}
// Input: {}
// Output: {}
// Input: {1, -1, 55}
// Output: {"One"}

// Complexity Analysis:
// The time complexity is O(n log n) because we use the sort function which is implemented as a variant of the QuickSort algorithm with a time complexity of O(n log n).
// The space complexity is O(n) because we use the vector 'valid_nums' to store the valid numbers and the vector 'result' to store the result.

// I'm not sure about the "strange number" requirement. If we should ignore the numbers that are not between 1 and 9 inclusive, then the provided code already does that. If we should keep them and just sort them, then we can remove the for loop that checks if the number is between 1 and 9 inclusive.
// If we should keep them and sort them in a way that they are sorted by the absolute value, then we can replace the sort line with sort(valid_nums.begin(), valid_nums.end(), [](int a, int b){return abs(