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

    string result="";
    int i,j;
    for (i=0;i<numbers.length();i++)
    if (numbers[i]!=' ')
    for (j=i+1;j<numbers.length();j++)
    if (numbers[j]!=' ')
    {
        if (num_map[numbers.substr(i,j-i)]>num_map[numbers.substr(j,j-i)])
        swap(numbers[i],numbers[j]);
    }
    return numbers;
}



