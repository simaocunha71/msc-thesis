    string vowels = "AEIOU";
    int i;
    for (i=0;i<word.length();i++)
    {
        if (find(vowels.begin(),vowels.end(),word[i])!=vowels.end())
        {
            string left=word.substr(0,i);
            string right=word.substr(i,word.length()-i);
            if (left.find_first_of(vowels)!=-1)
            return word[i];
            if (right.find_first_of(vowels)!=-1)
            return word[i];
        }
    }
    return "";
}


