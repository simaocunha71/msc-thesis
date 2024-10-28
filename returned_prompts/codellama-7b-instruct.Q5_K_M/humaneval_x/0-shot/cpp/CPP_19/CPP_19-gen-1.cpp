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

B:
    string sorted_numbers;
    string::size_type start = 0;
    while (start < numbers.size()){
        string::size_type end = numbers.find(' ', start);
        if (end == string::npos){
            end = numbers.size();
        }
        string number = numbers.substr(start, end - start);
        if (number_map.find(number) == number_map.end()){
            return "error";
        }
        sorted_numbers += to_string(number_map[number]);
        start = end + 1;
    }
    return sorted_numbers;
}

int main(){
    string numbers = "three one five";
    cout << sort_numbers(numbers) << endl;
    return 0;
}
