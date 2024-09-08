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
    string result;
    for(int i=0;i<numbers.size();i++){
        if(numbers[i]==' '){
            continue;
        }
        string num;
        while(numbers[i]!=' '&&i<numbers.size()){
            num+=numbers[i];
            i++;
        }
        if(num_map.find(num)!=num_map.end()){
            result+=to_string(num_map[num])+' ';
        }
    }
    return result;
}

