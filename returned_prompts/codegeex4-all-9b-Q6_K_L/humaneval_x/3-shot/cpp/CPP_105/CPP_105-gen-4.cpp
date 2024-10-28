    vector<int> numbers={};
    vector<string> names={};
    map<int,string> dict={};
    dict[1]="One";
    dict[2]="Two";
    dict[3]="Three";
    dict[4]="Four";
    dict[5]="Five";
    dict[6]="Six";
    dict[7]="Seven";
    dict[8]="Eight";
    dict[9]="Nine";
    for (int i=0;i<arr.size();i++)
    if (arr[i]>=1 && arr[i]<=9)
    numbers.push_back(arr[i]);
    sort(numbers.begin(), numbers.end());
    reverse(numbers.begin(), numbers.end());
    for (int i=0;i<numbers.size();i++)
    names.push_back(dict[numbers[i]]);
    return names;
}

