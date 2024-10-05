    int i;
    bool palindrome=true;
    for (i=0;i<text.length()/2;i++)
    if (text[i]!=text[text.length()-1-i])
    palindrome=false;
    return palindrome;
}


