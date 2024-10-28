    string vowel="aeiou";
    string result;
    int i;
    for (i=0;i<word.length();i++)
    if (vowel.find(word[i])!=string::npos && word[i-1]!='a' && word[i+1]!='a')
    {
        result=word[i];
        break;
    }
    return result;
}




