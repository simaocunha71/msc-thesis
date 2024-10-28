    string new_sentence;
    char chr;
    int i;
    for (i=0;i<sentence.length();i++)
    {
        chr=sentence[i];
        if (is_prime(chr))
        new_sentence+=chr;
    }
    return new_sentence;
}

bool is_prime(char chr)
{
    if (chr==' ')
    return false;
    if (chr=='A'||chr=='E'||chr=='O'||chr=='I'||chr=='U')
    return true;
    if (chr=='a'||chr=='e'||chr=='o'||chr=='i'||chr=='u')
    return true;
    if (chr=='0'||chr=='1'||chr=='2'||chr=='3'||chr=='4'||chr=='5'||chr=='6'||chr=='7'||chr=='8'||chr=='9')
    return false;
    return false;
}



