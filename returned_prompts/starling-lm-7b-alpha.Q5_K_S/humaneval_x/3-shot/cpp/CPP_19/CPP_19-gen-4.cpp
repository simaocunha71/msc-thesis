    map<string,string> number_map;
    number_map["zero"]="0";
    number_map["one"]="1";
    number_map["two"]="2";
    number_map["three"]="3";
    number_map["four"]="4";
    number_map["five"]="5";
    number_map["six"]="6";
    number_map["seven"]="7";
    number_map["eight"]="8";
    number_map["nine"]="9";

    string result;
    char chr;
    int i;
    for (i=0;i<numbers.length();i++)
    {
        chr=numbers[i];
        if (chr==' ')
        continue;
        if (number_map.count(string(""+chr))!=0)
        result+=number_map[string(""+chr)];
    }
    return result;
}


