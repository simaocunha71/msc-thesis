    map<string,int> m;
    m["zero"]=0;
    m["one"]=1;
    m["two"]=2;
    m["three"]=3;
    m["four"]=4;
    m["five"]=5;
    m["six"]=6;
    m["seven"]=7;
    m["eight"]=8;
    m["nine"]=9;
    string sorted_numbers="";
    string number;
    int i;
    for (i=0;i<numbers.length();i++)
    {
        number=numbers[i];
        sorted_numbers+=to_string(m[number]);
    }
    return sorted_numbers;
}



