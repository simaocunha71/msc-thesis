    int count = 0, apples = 0, oranges = 0;
    string word;
    for(int i = 0; i < s.length(); i++)
    {
        if(s[i] == ' ')
        {
            if(word == "apples")
            {
                apples = stoi(word.substr(0,word.find(" ")));
            }
            else if(word == "oranges")
            {
                oranges = stoi(word.substr(0,word.find(" ")));
            }
            word = "";
        }
        else
        {
            word += s[i];
        }
    }
    if(word == "apples")
    {
        apples = stoi(word.substr(0,word.find(" ")));
    }
    else if(word == "oranges")
    {
        oranges = stoi(word.substr(0,word.find(" ")));
    }
    return n - apples - oranges;
}