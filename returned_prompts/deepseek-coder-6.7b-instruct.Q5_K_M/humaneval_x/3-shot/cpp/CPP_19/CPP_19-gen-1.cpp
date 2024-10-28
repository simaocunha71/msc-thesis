    map<string, int> number_map;
    number_map["zero"] = 0;
    number_map["one"] = 1;
    number_map["two"] = 2;
    number_map["three"] = 3;
    number_map["four"] = 4;
    number_map["five"] = 5;
    number_map["six"] = 6;
    number_map["seven"] = 7;
    number_map["eight"] = 8;
    number_map["nine"] = 9;

    vector<string> number_strings;
    string temp="";
    for(int i=0; i<numbers.size(); i++){
        if(numbers[i] != ' '){
            temp+=numbers[i];
        }
        else{
            number_strings.push_back(temp);
            temp="";
        }
    }
    number_strings.push_back(temp);

    sort(number_strings.begin(), number_strings.end(), [&](const string &a, const string &b){
        return number_map[a] < number_map[b];
    });

    string sorted_numbers = "";
    for(int i=0; i<number_strings.size(); i++){
        sorted_numbers += number_strings[i];
        if(i < number_strings.size()-1){
            sorted_numbers += " ";
        }
    }

    return sorted_numbers;
}

