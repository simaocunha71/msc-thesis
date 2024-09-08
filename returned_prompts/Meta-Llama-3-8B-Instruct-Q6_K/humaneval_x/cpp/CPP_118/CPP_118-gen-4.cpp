    string result;
    int i = word.length() - 1;
    while(i > 0 && !isvowel(word[i]))
        i--;
    if(i == 0)
        return "";
    else
        result = word[i];

    return result;
}
bool isvowel(char ch)
{
    return (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' || ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U');
}

