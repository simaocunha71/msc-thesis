    vector<int> numbers;
    int i;
    for (i=0;i<arr.size();i++)
    if (arr[i]>0 && arr[i]<=9)
    numbers.push_back(arr[i]);

    sort(numbers.begin(),numbers.end());
    reverse(numbers.begin(),numbers.end());

    vector<string> names;
    map<int,string> numbers_map;
    numbers_map[1]="One";
    numbers_map[2]="Two";
    numbers_map[3]="Three";
    numbers_map[4]="Four";
    numbers_map[5]="Five";
    numbers_map[6]="Six";
    numbers_map[7]="Seven";
    numbers_map[8]="Eight";
    numbers_map[9]="Nine";

    for (i=0;i<numbers.size();i++)
    names.push_back(numbers_map[numbers[i]]);

    return names;
}


