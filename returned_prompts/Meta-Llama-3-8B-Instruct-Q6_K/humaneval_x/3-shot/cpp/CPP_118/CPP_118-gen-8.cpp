    string vowels="aeiouAEIOU";
    int i;
    for (i=word.length()-1;i>=0;i--)
    {
        if (find(vowels.begin(),vowels.end(),word[i])!=vowels.end())
        {
            int j=i-1;
            while (j>=0 && find(vowels.begin(),vowels.end(),word[j]) == vowels.end())
            j--;
            if (j>=0)
            return string(1,word[j]);
        }
    }
    return "";
}
