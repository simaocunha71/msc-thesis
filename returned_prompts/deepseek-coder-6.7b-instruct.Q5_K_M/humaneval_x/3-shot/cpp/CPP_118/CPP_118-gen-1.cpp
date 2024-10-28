    string vowels = "AEIOUaeiou";
    for (int i = word.size()-2; i > 0; --i)
        if (vowels.find(word[i]) != std::string::npos && 
            vowels.find(word[i-1]) == std::string::npos && 
            vowels.find(word[i+1]) == std::string::npos)
            return string(1, word[i]);
    return "";
}


