    string vowels="aeiou";
    string result="";
    int i;
    for (i=0;i<text.length();i++)
    if (vowels.find(text[i])==string::npos)
    result+=text[i];
    return result;
}

