    string vowels="aeiouAEIOU";
    string result;
    char chr;
    int i;
    for (i=word.length()-1;i>=1;i--)
    {
        chr=word[i];
        if (vowels.find(chr)>=0)
        {
        result=chr;
        break;
        }
    }
    return result;
}



