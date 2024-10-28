    int i;
    int j;
    string vowels="aeiouAEIOU";
    for (i=word.length()-1;i>=0;i--)
    {
        if (vowels.find(word[i])!=string::npos){
            for (j=i+1;j<word.length();j++){
                if (vowels.find(word[j])!=string::npos)
                return word[j];
            }
        }
    }
    return "";
}


