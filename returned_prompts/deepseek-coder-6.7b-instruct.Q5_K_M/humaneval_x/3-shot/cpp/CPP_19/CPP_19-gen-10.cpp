    map<string, int> numbers_dict = {{"zero",0}, {"one",1}, {"two",2}, {"three",3}, {"four",4}, {"five",5}, {"six",6}, {"seven",7}, {"eight",8}, {"nine",9}};
    vector<string> nums;
    string temp;
    for(int i=0; i<numbers.length(); i++){
        if(numbers[i] != ' '){
            temp += numbers[i];
        } else {
            nums.push_back(temp);
            temp = "";
        }
    }
    nums.push_back(temp);
    sort(nums.begin(), nums.end(), [&numbers_dict](const string &a, const string &b){return numbers_dict[a] < numbers_dict[b];});
    temp = "";
    for(string s: nums){
        temp += s + " ";
    }
    temp.pop_back();
    return temp;
}


