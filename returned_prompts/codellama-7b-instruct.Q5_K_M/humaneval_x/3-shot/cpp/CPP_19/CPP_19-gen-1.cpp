    map<string,int> number_map;
    string sorted_numbers;
    stringstream ss(numbers);
    string number;
    while (ss >> number)
    number_map[number]=number_map[number]+1;
    map<string,int>::iterator it;
    for (it=number_map.begin();it!=number_map.end();it++)
    sorted_numbers+=to_string(it->second)+" "+it->first;
    return sorted_numbers;
}



