    map<string, int> num_map = {
        {"zero", 0}, {"one", 1}, {"two", 2}, {"three", 3}, {"four", 4}, {"five", 5},
        {"six", 6}, {"seven", 7}, {"eight", 8}, {"nine", 9}
    };
    string result = "";
    vector<string> nums;
    string temp;
    for (int i = 0; i < numbers.length(); i++) {
        if (numbers[i] == ' ') {
            nums.push_back(temp);
            temp = "";
        } else {
            temp += numbers[i];
        }
    }
    nums.push_back(temp);
    sort(nums.begin(), nums.end(), 
         [&num_map](string a, string b) {
             return num_map[a] < num_map[b];
         });
    for (int i = 0; i < nums.size(); i++) {
        result += nums[i];
        if (i < nums.size() - 1) {
            result += ' ';
        }
    }
    return result;
}B:

C:
    map<string, int> num_map = {
        {"zero", 0}, {"one", 1}, {"two", 2}, {"three", 3}, {"four", 4}, {"five", 5},
        {"six", 6}, {"seven", 7}, {"eight", 8}, {"nine", 9}
    };
    string result = "";
    vector<string> nums;
    string temp;
    for (int i = 0; i < numbers.length(); i++) {
        if (numbers[i] == ' ') {
            nums.push_back(temp);
            temp = "";
        } else {
            temp += numbers[i];
        }
    }
    nums.push_back(temp);
    sort(nums.begin(), nums.end(), 
         [&num_map](string a, string b) {
             return num_map[a] < num_map[b];
         });
    for (int i = 0; i < nums.size(); i++) {
        result += nums[i];
        if (i < nums.size() - 1) {
            result += ' ';
        }
    }
    return result;
}

int main() {
    string numbers = "three one five";
    cout << sort_numbers(numbers) << endl;
    return 0;
}

D:
    map<string, int> num_map = {
        {"zero", 0},