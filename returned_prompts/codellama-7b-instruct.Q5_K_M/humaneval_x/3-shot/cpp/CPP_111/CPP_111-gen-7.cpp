    map<char,int> test_map;
    string test_str;
    char chr;
    int i;
    int counter=0;
    int max_counter=0;
    char max_char;
    char max_chars[1000];
    int count=0;
    for (i=0;i<test.length();i++)
    {
        chr=test[i];
        if (chr!=' ')
        {
            test_str+=chr;
            count++;
            if (test_map.find(chr)==test_map.end())
            {
                test_map[chr]=1;
            }
            else
            {
                test_map[chr]+=1;
            }
        }
    }
    for (auto it=test_map.begin();it!=test_map.end();it++)
    {
        if (it->second>max_counter)
        {
            max_counter=it->second;
            max_char=it->first;
        }
    }
    printf("%c %d",max_char,max_counter);
    return test_map;
}


