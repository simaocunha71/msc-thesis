    string vowels="aeiouAEIOU";
    string result="";
    for(int i=word.size()-2;i>0;i--)
    {
        if(vowels.find(word[i])==string::npos && vowels.find(word[i+1])==string::npos && vowels.find(word[i-1])==string::npos)
        {
            result=word[i];
            break;
        }
    }
    return result;
}


