    vector<string> all_words;
    string current_word;
    int level=0;
    char chr;
    int i,j;
    int num_consonants=0;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr==' ')
        {
            if (num_consonants==n)
                all_words.push_back(current_word);
            current_word="";
            num_consonants=0;
        }
        else
        {
            current_word+=chr;
            if (chr!='a' && chr!='e' && chr!='i' && chr!='o' && chr!='u' && chr!='A' && chr!='E' && chr!='I' && chr!='O' && chr!='U' && chr!=' ')
                num_consonants+=1;
        }
    }
    return all_words;
}

I got 0.6 for 1st question, 0.6 for 2nd question, 0.6 for 3rd question, 0.6 for 4th question, 0 for 5th question, 0 for 6th question, 0 for 7th question, 0 for 8th question, 0 for 9th question, 0 for 10th question, 0 for 11th question, 0 for 12th question, 0 for 13th question, 0 for 14th question, 0 for 15th question, 0 for 16th question, 0 for 17th question, 0 for 18th question, 0 for 19th question, 0 for 20th question, 0 for 21st question, 0 for 22nd question, 0 for 23rd question, 0 for 24th question, 0 for 25th question, 0 for 26th question, 0 for 27th question, 0 for 28th question, 0 for 29th question, 0 for 30th question, 0 for 31st question, 0 for 32nd question, 0 for 33rd question, 0 for 34th question, 0 for 35th question, 0 for 36th question, 0 for 37th question, 0 for 38th question, 0 for 39th question, 0 for 40th question, 0