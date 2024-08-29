string encrypt(string s){
    string result = "";
    for(int i = 0; i < s.size(); i++){
        // Check if the character is a letter
        if(isalpha(s[i])){
            // Convert the character to uppercase if it's a lowercase letter
            if(islower(s[i])){
                s[i] = toupper(s[i]);
            }
            // Convert the character to its corresponding encrypted character
            s[i] = ((s[i] - 'A') + 4) % 26 + 'A';
        }
        // Append the encrypted character to the result string
        result += s[i];
    }
    return result;
}

C:
string encrypt(string s){
    string result = "";
    for(int i = 0; i < s.size(); i++){
        // Check if the character is a letter
        if(isalpha(s[i])){
            // Convert the character to uppercase if it's a lowercase letter
            if(islower(s[i])){
                s[i] = toupper(s[i]);
            }
            // Convert the character to its corresponding encrypted character
            s[i] = ((s[i] - 'A') + 4) % 26 + 'A';
        }
        // Append the encrypted character to the result string
        result += s[i];
    }
    return result;
}

E:
string encrypt(string s){
    string result = "";
    for(int i = 0; i < s.size(); i++){
        // Check if the character is a letter
        if(isalpha(s[i])){
            // Convert the character to uppercase if it's a lowercase letter
            if(islower(s[i])){
                s[i] = toupper(s[i]);
            }
            // Convert the character to its corresponding encrypted character
            s[i] = ((s[i] - 'A') + 4) % 26 + 'A';
        }
        // Append the encrypted character to the result string
        result += s[i];
    }
    return result;
}

F:
string encrypt(string s){
    string result = "";
    for(int i = 0; i < s.size(); i++){
        // Check if the character is a letter
        if(isalpha(s[i])){
            // Convert the character to uppercase if it's a lowercase letter
            if(islower(s[i])){
                s[i] = toupper(s[i]);
            }
            // Convert the character to its corresponding encrypted character
            s[i] = ((s[i] - 'A