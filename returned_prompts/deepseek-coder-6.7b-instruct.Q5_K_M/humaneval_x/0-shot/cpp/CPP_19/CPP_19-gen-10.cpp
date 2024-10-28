    map<string, string> text_numbers;
    text_numbers["zero"] = "0";
    text_numbers["one"] = "1";
    text_numbers["two"] = "2";
    text_numbers["three"] = "3";
    text_numbers["four"] = "4";
    text_numbers["five"] = "5";
    text_numbers["six"] = "6";
    text_numbers["seven"] = "7";
    text_numbers["eight"] = "8";
    text_numbers["nine"] = "9";

    map<string, string> num_texts;
    num_texts["0"] = "zero";
    num_texts["1"] = "one";
    num_texts["2"] = "two";
    num_texts["3"] = "three";
    num_texts["4"] = "four";
    num_texts["5"] = "five";
    num_texts["6"] = "six";
    num_texts["7"] = "seven";
    num_texts["8"] = "eight";
    num_texts["9"] = "nine";

    string word = "";
    string temp = "";
    string result = "";
    for(int i = 0; i < numbers.size(); i++){
        if(numbers[i] == ' '){
            word += temp;
            temp = "";
        } else {
            temp += numbers[i];
            if(i == numbers.size()-1){
                word += temp;
            }
        }
    }

    string arr[word.size()];
    int index = 0;
    for(int i = 0; i < word.size(); i++){
        if(word[i] == ' ' || i == word.size()-1){
            if(i == word.size()-1){
                arr[index] = word.substr(i-index, index+1);
            } else {
                arr[index] = word.substr(i-index, index);
            }
            index = 0;
