    string vowels="aeiouAEIOU";
    string new_text=text;
    for (int i=0;i<new_text.length();i++)
    {
        if (vowels.find(new_text[i])!=string::npos)
        {
            new_text.erase(i,1);
            i-=1;
        }
    }
    return new_text;
}