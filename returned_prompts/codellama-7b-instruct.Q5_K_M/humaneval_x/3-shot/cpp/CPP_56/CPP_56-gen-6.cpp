    int left_brackets=0;
    int right_brackets=0;
    for (int i=0;i<brackets.length();i++)
    {
        if (brackets[i]=='<')
        left_brackets++;
        if (brackets[i]=='>')
        right_brackets++;
    }
    if (left_brackets==right_brackets)
    return true;
    return false;
}




