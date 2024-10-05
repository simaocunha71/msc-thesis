    string new_text="";
    string vowels="aeiouAEIOU";
    for (int i=0;i<text.length();i++)
    {
        if (find(vowels.begin(),vowels.end(),text[i])==vowels.end())
        new_text+=text[i];
    }
    return new_text;
}

