    string without_vowels;
    char chr;
    char vowels[]={'a','e','i','o','u'};
    int i,j;
    for (i=0;i<text.length();i++)
    {
        chr=text[i];
        for (j=0;j<5;j++)
        if (chr==vowels[j])
        {
            without_vowels+="";
            break;
        }
        else
        {
            without_vowels+=chr;
        }
    }
    return without_vowels;
}



