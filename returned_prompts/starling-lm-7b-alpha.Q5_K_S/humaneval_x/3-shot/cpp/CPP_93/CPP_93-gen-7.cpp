    string result="";
    char chr;
    char vowel_char;
    char vowel_char_new;
    for (int i=0;i<message.length();i++)
    {
        chr=message[i];
        if (chr>=97 && chr<=122)
        {
            vowel_char=chr;
            vowel_char_new=0;
            vowel_char_new=vowel_char;
            vowel_char_new+=2;
            if (vowel_char_new==123)
            vowel_char_new-=26;
            result+=vowel_char_new;
        }
        else
        {
            result+=chr;
        }
    }
    return result;
}



