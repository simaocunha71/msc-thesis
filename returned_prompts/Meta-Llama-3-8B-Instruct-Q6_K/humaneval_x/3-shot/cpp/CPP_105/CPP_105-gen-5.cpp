    vector<string> result;
    map<string, int> num_to_name = {{"One", 1}, {"Two", 2}, {"Three", 3}, {"Four", 4}, {"Five", 5}, {"Six", 6}, {"Seven", 7}, {"Eight", 8}, {"Nine", 9}};
    vector<int> sorted_arr(arr.begin(), arr.end());
    sort(sorted_arr.begin(), sorted_arr.end());
    reverse(sorted_arr.begin(), sorted_arr.end());
    for (int num : sorted_arr) {
        if (num >= 1 && num <= 9) {
            result.push_back(num_to_name.find(to_string(num))->second == 1 ? "One" : num_to_name.find(to_string(num))->second == 2 ? "Two" : num_to_name.find(to_string(num))->second == 3 ? "Three" : num_to_name.find(to_string(num))->second == 4 ? "Four" : num_to_name.find(to_string(num))->second == 5 ? "Five" : num_to_name.find(to_string(num))->second == 6 ? "Six" : num_to_name.find(to_string(num))->second == 7 ? "Seven" : num_to_name.find(to_string(num))->second == 8 ? "Eight" : "Nine");
        }
    }
    return result;
}