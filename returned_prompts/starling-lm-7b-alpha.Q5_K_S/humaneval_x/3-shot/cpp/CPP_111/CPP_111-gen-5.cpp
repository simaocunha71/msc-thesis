    map<char,int> char_map;
    char chr;
    int i,count;
    for (i=0;i<test.length();i++)
    {
        chr=test[i];
        if (chr==' ') continue;
        if (char_map.find(chr)==char_map.end()){
        char_map[chr]=1;
        }
        else
        {
        count=char_map[chr];
        char_map[chr]=count+1;
        }
    }

    return char_map;
}


