    map<string,int> number_map;
    number_map["zero"]=0;
    number_map["one"]=1;
    number_map["two"]=2;
    number_map["three"]=3;
    number_map["four"]=4;
    number_map["five"]=5;
    number_map["six"]=6;
    number_map["seven"]=7;
    number_map["eight"]=8;
    number_map["nine"]=9;
    string result;
    vector<string> numbers_list;
    string chr;
    int i;
    for (i=0;i<numbers.length();i++)
    {
        chr=numbers[i];
        if (chr!=' ')
        {
            numbers_list.push_back(chr);
        }
    }
    sort(numbers_list.begin(),numbers_list.end(),[&number_map](string a, string b){return number_map[a]<number_map[b];});
    for (i=0;i<numbers_list.size();i++)
    {
        result+=numbers_list[i];
        if (i<numbers_list.size()-1)
        result+=" ";
    }
    return result;
} // not optimized for performance and code readability


