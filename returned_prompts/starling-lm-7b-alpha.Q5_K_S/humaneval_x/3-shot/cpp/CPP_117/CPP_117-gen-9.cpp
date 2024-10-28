    vector<string> all_words;
    vector<string> current_words;
    int i,j;
    char chr;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr==' ')
        {
            if (current_words.size()!=0)
            {
                int count=0;
                for (j=0;j<current_words.size();j++)
                {
                    if (is_consonant(current_words[j][0])==true){count+=1;}
                }
                if (count==n)
                {
                    all_words.push_back(current_words[0]);
                }
            }
            current_words.clear();
        }
        else {
        current_words.push_back(chr);
        }
    }
    return all_words;
}

bool is_consonant(char chr)
{
    if (chr=='a'||chr=='e'||chr=='i'||chr=='o'||chr=='u'||chr=='y')
    return false;
    return true;
}




