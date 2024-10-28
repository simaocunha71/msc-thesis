    string vowels="AEIOUaeiou";
    int i;
    for (i=1;i<word.length()-1;i++)
    if (vowels.find(word[i])>=0&&word[i-1]!='a'&&word[i+1]!='a')
    return word[i];
    return "";
}

