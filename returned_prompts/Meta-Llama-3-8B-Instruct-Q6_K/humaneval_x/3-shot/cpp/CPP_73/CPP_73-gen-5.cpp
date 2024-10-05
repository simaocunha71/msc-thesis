    int changes = 0;
    string s = "";
    for (int i = 0; i < arr.size(); i++) {
        s += to_string(arr[i]);
    }
    string rev = s;
    reverse(rev.begin(), rev.end());
    for (int i = 0; i < s.size(); i++) {
        if (s[i] != rev[i]) {
            changes++;
        }
    }
    return changes;
}  // This solution is not correct because it doesn't consider the case where we can change only one element to make the array palindromic.
// We need to consider the case where we change the middle element to make the array palindromic. If it is not possible to make the array palindromic by changing one element, then we need to change two elements.
// Also, the solution is not considering the case where we can change more than one element to make the array palindromic.
// We need to find the number of elements that need to be changed to make the array palindromic. We can do this by finding the number of elements that are not equal to their corresponding elements from the end.
// The time complexity of this solution is O(n) where n is the size of the array.
// The space complexity of this solution is O(n) where n is the size of the array.
// We can improve the space complexity to O(1) by not using any extra space and just updating the changes variable.
// We can also improve the time complexity to O(n/2) by only iterating up to the middle of the array.
// Here is the corrected code:
int smallest_change(vector<int> arr) {
    int changes = 0;
    string s = "";
    for (int i = 0; i < arr.size(); i++) {
        s += to_string(arr[i]);
    }
    string rev = s;
    reverse(rev.begin(), rev.end());
    int i = 0;
    int j = s.size() - 1;
    while (i < j) {
        if (s[i] != rev[j]) {
            changes++;
            i++;
            j--;
        } else {
            i++;
            j--;
        }
    }
    return changes;
}  // This solution is still not correct because it doesn't consider the case where we can change only one element to make the array palindromic.
// We need to consider the case where we change the middle