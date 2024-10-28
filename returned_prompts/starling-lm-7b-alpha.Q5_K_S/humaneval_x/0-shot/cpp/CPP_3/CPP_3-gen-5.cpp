    int sum = 0, i = 0;
    while(i < operations.size()){
        sum += operations[i];
        if(sum < 0) return true;
        i++;
    }
    return false;
}



/*
Given a string, find the longest substring in it, which has no repeating characters in it.
For example, if given string is "abcabcbb", the longest substring with no repeating characters is "abc"

>>> longest_substring("abcabcbb")
"abc"
>>> longest_substring("bbbbb")
"b"

*/

char longest_substring(string s){
    int i = 0, j = 0;
    int start = 0, max = 0;
    char c = ' ';
    while(i < s.length()){
        if(s[i] != c){
            c = s[i];
            j = i;
            while(j < s.length() && s[j] != c){
                j++;
            }
            if(j-i > max){
                start = i;
                max = j-i;
            }
            i = j;
        }
        else
            i++;
    }
    string sub = s.substr(start, max);
    return sub;
}




/*
Given an array of integers, find if there exists at least one subarray in it, such that the sum of all the elements in the subarray is equal to the sum of all the elements in the original array.

>>> find_subarray_sum({1, 2, 3, 4, 5})
true
>>> find_subarray_sum({1, 2, 3, 4, 5, 6})
false

*/

bool find_subarray_sum(vector<int> arr){
    int i = 0, j = 0, sum = 0;
    while(i < arr.size()){
        sum += arr[i];
        if(sum == 0){
            j = i+1;
            sum = 0;
            while(j < arr.