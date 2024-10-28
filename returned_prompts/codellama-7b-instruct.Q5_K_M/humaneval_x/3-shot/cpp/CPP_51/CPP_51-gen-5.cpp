    string vowels = "aeiouAEIOU";
    auto pred = [&vowels](char c){return vowels.find(c) != string::npos;};
    return text.erase(remove_if(text.begin(), text.end(), pred), text.end());
}


