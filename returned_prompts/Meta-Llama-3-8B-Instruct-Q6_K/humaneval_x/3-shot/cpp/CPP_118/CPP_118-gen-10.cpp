    int i;
    string result="";
    for(i=word.length()-1;i>0;i--)
    {
        if(isvowel(word[i]))
        {
            if(isvowel(word[i-1]))
            {
                return "";
            }
            else
            {
                return word.substr(i);
            }
        }
    }
    return result;
}

bool isvowel(char c)
{
    c = tolower(c);
    return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');
}
// This is a function to check if a character is a vowel or not. It converts the character to lower case first to handle the case sensitivity. .


