    int count=0;
    string vowels = "aeiou";
    transform(s.begin(), s.end(), s.begin(), ::tolower);
    for(char& c : s)
    {
        if(vowels.find(c)!=std::string::npos)
        {
            count++;
        }
    }
    if(s[s.length()-1]=='y')
    {
        count++;
    }
    return count;
}


