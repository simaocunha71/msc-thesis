    string result;
    for(int i=0; i<s.length(); i++){
        if(isalpha(s[i])){
            result += (islower(s[i])) ? toupper(s[i]) : tolower(s[i]);
        } else {
            result += s[i];
        }
    }
    reverse(result.begin(), result.end());
    return result;
}  // Time complexity: O(n) where n is the length of the string. Space complexity: O(n) for the result string.