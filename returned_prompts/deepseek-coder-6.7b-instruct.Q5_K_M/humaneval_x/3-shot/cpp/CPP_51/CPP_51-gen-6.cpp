    string vowels="aeiouAEIOU";
    for  (char & c : text) 
    {
        if  (vowels.find(c)!=string::npos) 
        {
            c=' ';
        }
    }
    return text;
}

