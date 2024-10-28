    string vowels = "aeiouAEIOU";
    transform(text.begin(), text.end(), text.begin(), [&vowels](char c) {
        return vowels.find(c) == string::npos ? c : ' ';
    });
    return text;
}


