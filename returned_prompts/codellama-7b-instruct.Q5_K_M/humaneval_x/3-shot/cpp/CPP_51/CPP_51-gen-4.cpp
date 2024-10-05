    string vowels="aeiou";
    for (int i=0;i<vowels.length();i++)
    {
        auto it=find(text.begin(),text.end(),vowels[i]);
        if (it!=text.end())
        text.erase(it);
    }
    return text;
}


