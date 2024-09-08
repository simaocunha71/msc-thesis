    map<string, int> num_map;
    num_map["zero"] = 0;
    num_map["one"] = 1;
    num_map["two"] = 2;
    num_map["three"] = 3;
    num_map["four"] = 4;
    num_map["five"] = 5;
    num_map["six"] = 6;
    num_map["seven"] = 7;
    num_map["eight"] = 8;
    num_map["nine"] = 9;
    string sorted_numbers = "";
    vector<string> numbers_vector;
    string temp;
    for(int i = 0; i < numbers.length(); i++){
        if(numbers[i] == ' '){
            numbers_vector.push_back(temp);
            temp = "";
        }else{
            temp += numbers[i];
        }
    }
    numbers_vector.push_back(temp);

    for(int i = 0; i < numbers_vector.size(); i++){
        for(int j = 0; j < numbers_vector.size(); j++){
            if(num_map[numbers_vector[i]] < num_map[numbers_vector[j]]){
                string temp = numbers_vector[i];
                numbers_vector[i] = numbers_vector[j];
                numbers_vector[j] = temp;
            }
        }
    }

    for(int i = 0; i < numbers_vector.size(); i++){
        sorted_numbers += numbers_vector[i] + " ";
    }
    return sorted_numbers;
}
int main()
{
    string numbers = "three one five";
    cout<< sort_numbers(numbers);
    return 0;
}

B:
    #include <iostream>
    #include <string>
    #include <vector>
    #include <algorithm>

    std::string sort_numbers(std::string numbers) {
        std::vector<std::string> numVector;
        std::string temp;

        // Split the string into individual numbers
        for (int i = 0; i < numbers.length(); i++) {
            if (numbers[i] == ' ') {
                numVector.push_back(temp);
                temp = "";
            } else {
                temp += numbers[i];
            }
        }
        numVector.push_back(temp);

        // Sort the numbers
        std::sort(numVector.begin(), numVector.end(),
            [](const std::string& a, const std::string& b) {
                return std::stoi(a) < std::stoi(b);
            });

        // Join the numbers back into a string
        std::string