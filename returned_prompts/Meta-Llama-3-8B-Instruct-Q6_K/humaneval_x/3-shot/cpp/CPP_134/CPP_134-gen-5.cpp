    if(txt.empty())
    return false;
    if(txt.back() >= 'a' && txt.back() <= 'z' || txt.back() >= 'A' && txt.back() <= 'Z')
    {
        if(txt.find_last_not_of(" ") != string::npos && txt.find_last_not_of(" ") != txt.size()-1)
        return false;
        return true;
    }
    return false;
}
// Explanation: 
// 1. Check if the string is empty, if yes, return false.
// 2. Check if the last character of the string is an alphabetical character.
// 3. If the last character is a letter, check if it's part of a word.
// 4. If the last character is part of a word, return false, else return true.