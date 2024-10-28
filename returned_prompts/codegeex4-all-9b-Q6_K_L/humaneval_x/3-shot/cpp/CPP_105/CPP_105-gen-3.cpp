    vector<string> new_arr;
    map<int,string> name_map;
    name_map[1]="One";
    name_map[2]="Two";
    name_map[3]="Three";
    name_map[4]="Four";
    name_map[5]="Five";
    name_map[6]="Six";
    name_map[7]="Seven";
    name_map[8]="Eight";
    name_map[9]="Nine";

    vector<int> new_arr2;
    int i;
    for (i=0;i<arr.size();i++)
    if (arr[i]>0 && arr[i]<10)
    new_arr2.push_back(arr[i]);
    sort(new_arr2.begin(),new_arr2.end());
    reverse(new_arr2.begin(),new_arr2.end());
    for (i=0;i<new_arr2.size();i++)
    new_arr.push_back(name_map[new_arr2[i]]);
    return new_arr;
}

