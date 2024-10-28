    map<string,int> map_string_to_int;
    map_string_to_int["zero"]=0;
    map_string_to_int["one"]=1;
    map_string_to_int["two"]=2;
    map_string_to_int["three"]=3;
    map_string_to_int["four"]=4;
    map_string_to_int["five"]=5;
    map_string_to_int["six"]=6;
    map_string_to_int["seven"]=7;
    map_string_to_int["eight"]=8;
    map_string_to_int["nine"]=9;

    vector<string> all_numbers;
    char chr;
    int i;
    for (i=0;i<numbers.length();i++)
    {
        chr=numbers[i];
        if (chr==' ')
        {
            continue;
        }
        all_numbers.push_back(string(1,chr));
    }

    for (i=0;i<all_numbers.size();i++)
    for (int j=i+1;j<all_numbers.size();j++)
    {
        if (map_string_to_int[all_numbers[i]]>map_string_to_int[all_numbers[j]])
        {
            char tmp;
            tmp=all_numbers[i];
            all_numbers[i]=all_numbers[j];
            all_numbers[j]=tmp;
        }
    }

    string result;
    for (i=0;i<all_numbers.size();i++)
    {
        result+=all_numbers[i];
        if (i!=all_numbers.size()-1)
        {
            result+=' ';
        }
    }

    return result;
}


