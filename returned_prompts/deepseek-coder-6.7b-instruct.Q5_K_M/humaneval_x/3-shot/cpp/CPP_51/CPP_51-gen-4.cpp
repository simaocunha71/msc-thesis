    string vowels = "aeiouAEIOU";
    for (int i = 0; i < vowels.size(); i++)
    {
        text.erase(remove(text.begin(), text.end(), vowels[i]), text.end());
    }
    return text;
}


