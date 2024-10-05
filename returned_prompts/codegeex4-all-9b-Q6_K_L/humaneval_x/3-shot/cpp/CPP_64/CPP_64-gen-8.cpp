    string vowels="aeiouAEIOU";
    int count=0;
    int i;
    for (i=0;i<s.length();i++)
    {
        if (s[i]=='y' || s[i]=='Y')
        {
            if (i==s.length()-1){
                count+=1;
            }
        }
        else{
            if (find(vowels.begin(),vowels.end(),s[i])!=vowels.end())
            {
                count+=1;
            }
        }
    }
    return count;
}

