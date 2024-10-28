    map<string, int> number_map;
    string nums[10]={"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    int i;
    for (i=0;i<10;i++)
    number_map[nums[i]]=i;
    string sorted_numbers;
    for (i=0;i<numbers.length();i++)
    sorted_numbers+=nums[number_map[numbers[i]]];
    return sorted_numbers;
}








