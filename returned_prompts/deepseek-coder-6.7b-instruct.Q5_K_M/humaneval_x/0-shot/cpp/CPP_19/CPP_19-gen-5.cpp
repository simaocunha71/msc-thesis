    map<string, int> str_to_num;
    str_to_num["zero"] = 0;
    str_to_num["one"] = 1;
    str_to_num["two"] = 2;
    str_to_num["three"] = 3;
    str_to_num["four"] = 4;
    str_to_num["five"] = 5;
    str_to_num["six"] = 6;
    str_to_num["seven"] = 7;
    str_to_num["eight"] = 8;
    str_to_num["nine"] = 9;

    map<int, string> num_to_str;
    num_to_str[0] = "zero";
    num_to_str[1] = "one";
    num_to_str[2] = "two";
    num_to_str[3] = "three";
    num_to_str[4] = "four";
    num_to_str[5] = "five";
    num_to_str[6] = "six";
    num_to_str[7] = "seven";
    num_to_str[8] = "eight";
    num_to_str[9] = "nine";

    string word = "";
    string sorted_numbers = "";
    for(int i = 0; i < numbers.length(); i++){
        if(numbers[i] == ' '){
            sorted_numbers += num_to_str[str_to_num[word]] + " ";
            word = "";
        }
        else{
            word += numbers[i];
        }
    }
    sorted_numbers += num_to_str[str_to_num[word]];
    return sorted_numbers;
}
int main(){
    printf("%s\n", sort_numbers("three one five").c_str());
    return 0;
}
```

### Python
