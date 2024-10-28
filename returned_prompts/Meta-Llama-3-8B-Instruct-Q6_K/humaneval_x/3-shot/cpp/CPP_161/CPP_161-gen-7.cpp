    string result;
    for(int i=0; i<s.length(); i++){
        if(isalpha(s[i])){
            if(islower(s[i])) result += toupper(s[i]);
            else result += tolower(s[i]);
        }
        else result += s[i];
    }
    reverse(result.begin(), result.end());
    return result;
}  // This is the correct answer. It correctly handles the case where the input string contains no letters.