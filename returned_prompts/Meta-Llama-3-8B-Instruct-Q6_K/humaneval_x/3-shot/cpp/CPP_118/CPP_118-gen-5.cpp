    int i;
    string closest_vowel = "";
    for (i=word.length()-1; i>=0; i--)
    {
        char chr = word[i];
        if (chr == 'a' || chr == 'e' || chr == 'i' || chr == 'o' || chr == 'u' || chr == 'A' || chr == 'E' || chr == 'I' || chr == 'O' || chr == 'U')
        {
            int j;
            bool found_consonant = false;
            for (j=i-1; j>=0; j--)
            {
                if (isalpha(word[j]) && !isvowel(word[j]))
                {
                    found_consonant = true;
                    break;
                }
            }
            if (found_consonant)
            {
                closest_vowel = word.substr(i, 1);
                break;
            }
        }
    }
    return closest_vowel;
}