
// Create a map to store the corresponding values of words from 0 to 9.
    map<string, int> num_map = {
        {"zero", 0},
        {"one", 1},
        {"two", 2},
        {"three", 3},
        {"four", 4},
        {"five", 5},
        {"six", 6},
        {"seven", 7},
        {"eight", 8},
        {"nine", 9}
    };
    
    // Create a vector to store the numbers in order.
    vector<string> num_vec;
    
    // Create a stream to parse the string.
    istringstream ss(numbers);
    string word;
    
    // While there are still words, parse them.
    while (ss >> word) {
        // Add the corresponding number to the vector.
        num_vec.push_back(num_map[word]);
    }
    
    // Sort the vector.
    sort(num_vec.begin(), num_vec.end());
    
    // Create a string to store the result.
    string result = "";
    
    // For each number in the vector, add the corresponding word to the result.
    for (int num : num_vec) {
        for (auto it = num_map.begin(); it != num_map.end(); ++it) {
            if (it->second == num) {
                result += it->first + " ";
                break;
            }
        }
    }
    
    // Return the result without the trailing space.
    return result.substr(0, result.length() - 1);
}

int main() {
    cout << sort_numbers("three one five") << endl;  // Outputs: "one three five"
    return 0;
}

This program works by first creating a map to store the corresponding values of words from 0 to 9. It then creates a vector to store the numbers in order. The string is parsed into words using a string stream, and the corresponding number is added to the vector. The