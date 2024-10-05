    map<string,int> num_map;
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
    string smallest_to_largest[10];
    int i,j;
    for (i=0;i<numbers.length();i++)
    {
        string current_number=numbers[i];
        smallest_to_largest[num_map[current_number]]=current_number;
    }
    string sorted_numbers;
    for (i=0;i<10;i++)
    {
        sorted_numbers+=smallest_to_largest[i];
    }
    return sorted_numbers;
}


