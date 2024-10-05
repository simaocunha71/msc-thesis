    map<string, int> num_map;
    num_map["zero"]=0;
    num_map["one"]=1;
    num_map["two"]=2;
    num_map["three"]=3;
    num_map["four"]=4;
    num_map["five"]=5;
    num_map["six"]=6;
    num_map["seven"]=7;
    num_map["eight"]=8;
    num_map["nine"]=9;
    vector<string> num_list;
    string num;
    int i;
    for (i=0;i<numbers.length();i++)
    {
        if (numbers[i]==' ')
        continue;
        num+=numbers[i];
        if (i==numbers.length()-1 || numbers[i+1]==' ')
        {
            num_list.push_back(num);
            num="";
        }
    }
    sort(num_list.begin(), num_list.end(), [](string a, string b) { return num_map[a]<num_map[b]; });
    string sorted_num;
    for (i=0;i<num_list.size();i++)
    sorted_num+=num_list[i]+" ";
    return sorted_num;
}