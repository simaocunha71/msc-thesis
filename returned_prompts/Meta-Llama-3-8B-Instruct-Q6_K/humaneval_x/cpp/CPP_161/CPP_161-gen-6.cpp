    // Create a string builder
    string result;
    for(int i = 0; i < s.length(); i++){
        // Check if the character is a letter
        if(isalpha(s[i])){
            // Reverse the case
            if(islower(s[i])) {
                result += toupper(s[i]);
            } else {
                result += tolower(s[i]);
            }
        } else {
            // If not a letter, just add it as it is
            result += s[i];
        }
    }
    return result;
}

int main() {
    string s = "#a@C";
    string res = solve(s);
    printf("%s\n", res.c_str());
    return 0;
}

