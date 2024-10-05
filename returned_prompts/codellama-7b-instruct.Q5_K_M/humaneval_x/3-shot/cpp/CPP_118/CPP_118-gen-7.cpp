    int i,j,k;
    string vowel="aeiou";
    int max_distance=0;
    string closest_vowel;
    for (i=0;i<word.length();i++)
    {
        if (vowel.find(word[i])!=-1)
        {
            if (i==0)
            continue;
            if (i==word.length()-1)
            continue;
            for (j=i+1;j<word.length();j++)
            {
                if (vowel.find(word[j])!=-1)
                {
                    int distance=abs(i-j);
                    if (distance>max_distance)
                    {
                        max_distance=distance;
                        closest_vowel=word[j];
                    }
                }
            }
        }
    }
    return closest_vowel;
}



