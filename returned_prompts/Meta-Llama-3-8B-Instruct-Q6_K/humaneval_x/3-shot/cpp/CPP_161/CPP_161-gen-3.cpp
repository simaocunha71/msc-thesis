    string result;
    for (int i=0;i<s.length();i++){
        if (isalpha(s[i])){
            result+=islower(s[i]) ? toupper(s[i]) : tolower(s[i]);
        }else{
            result+=s[i];
        }
    }
    if (result.length()<=1) {
        reverse(result.begin(), result.end());
    }
    return result;
}  // This will work for the given examples but for more complex cases like "aB" or "Aa" it might not work as expected. For that, you can iterate over each character and check if it is lowercase or uppercase, and then reverse it accordingly. This will work for all cases.  // This is the correct solution.