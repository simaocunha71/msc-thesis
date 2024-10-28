    str.erase(
        remove_if(str.begin(), str.end(), [](char c) { return !isalpha(c); }),
        str.end());
    str.erase(
        remove_if(str.begin(), str.end(), [](char c) { return !isupper(c) && !islower(c); }),
        str.end());
    sort(str.begin(), str.end());
    return unique(str.begin(), str.end()) - str.begin();
}


/*
Given an array of integers, return the maximum sum of a subarray of that array, using a divide-and-conquer approach.
>>> maxSubArraySum(new int[] {-2, 1, -3, 4, -1, 2, 1, -5, 4})
6
>>> maxSubArraySum(new int[] {-2, 3, 4, -1, -2, 1, 5, -3})
7
*/
int maxSubArraySum(int arr[], int n) {
    if(n==1)
    return arr[0];
    else {
        int a1=maxSubArraySum(arr,n/2);
        int a2=maxSubArraySum(arr+n/2,n-n/2);
        return max(a1,a2)+max(max(a1,a2),arr[n/2]);
    }
}

/*
Given an array of strings, return an array of the strings that have equal lengths.
>>> filterEqualLengthStrings(new string[] {"cat", "dog", "elephant", "bear"})
["cat", "dog"]
>>> filterEqualLengthStrings(new string[] {"hello", "world", "moon"})
[]
*/
vector<string> filterEqualLengthStrings(vector<string> strs) {
    sort(strs.begin(), strs.end(), [](string s1, string s2) { return s1.length() < s2.length(); });
    vector<string> res;
    for (int i = 0, j = 0; i < strs.size(); i++) {
        if (strs[i