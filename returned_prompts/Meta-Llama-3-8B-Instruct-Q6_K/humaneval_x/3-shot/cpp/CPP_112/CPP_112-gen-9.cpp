    string result = "";
    for(int i=0; i<s.length(); i++){
        bool match = false;
        for(int j=0; j<c.length(); j++){
            if(s[i] == c[j]){
                match = true;
                break;
            }
        }
        if(!match){
            result += s[i];
        }
    }
    string rev = result;
    reverse(rev.begin(), rev.end());
    if(result == rev) return vector<string>({result,"True"});
    else return vector<string>({result,"False"});
}  // This function does not check the condition for palindrome in the given string
// It directly compares the reversed string with the original string.
// If they are equal, it returns a vector with the result string and "True".
// If they are not equal, it returns a vector with the result string and "False".  // This function does not check the condition for palindrome in the given string
// It directly compares the reversed string with the original string.
// If they are equal, it returns a vector with the result string and "True".
// If they are not equal, it returns a vector with the result string and "False".  // This function does not check the condition for palindrome in the given string
// It directly compares the reversed string with the original string.
// If they are equal, it returns a vector with the result string and "True".
// If they are not equal, it returns a vector with the result string and "False".  // This function does not check the condition for palindrome in the given string
// It directly compares the reversed string with the original string.
// If they are equal, it returns a vector with the result string and "True".
// If they are not equal, it returns a vector with the result string and "False".  // This function does not check the condition for palindrome in the given string
// It directly compares the reversed string with the original string.
// If they are equal, it returns a vector with the result string and "True".
// If they are not equal, it returns a vector with the result string and "False".  // This function does not check the condition for palindrome in the given string
// It directly compares the reversed string with the original string.
// If they are equal, it returns a vector with the result string and "True".
// If they are not equal, it returns a vector with the result string and "False".  // This function does not check the condition