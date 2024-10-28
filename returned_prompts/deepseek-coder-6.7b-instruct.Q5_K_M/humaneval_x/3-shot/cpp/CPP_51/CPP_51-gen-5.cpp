    string vowels="aeiouAEIOU";
    for  (int i=0;i<vowels.size();i++)
    {
        while  (text.find(vowels[i])<text.size())
        {
            text.erase(text.find(vowels[i]),1);
        }
    }
    return text;
}



