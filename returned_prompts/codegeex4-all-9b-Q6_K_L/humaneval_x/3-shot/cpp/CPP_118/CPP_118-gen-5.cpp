    string vowels="aeiou";
    int i;
    for (i=word.length()-1;i>=1;i--)
    {
        if (vowels.find(word[i])<vowels.length())
        {
            if (vowels.find(word[i-1])<vowels.length())
            {
                return word[i];
            }
        }
    }
    return "";
}

