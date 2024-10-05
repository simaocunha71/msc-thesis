    map<int,string> num={};
    num[1]="One";
    num[2]="Two";
    num[3]="Three";
    num[4]="Four";
    num[5]="Five";
    num[6]="Six";
    num[7]="Seven";
    num[8]="Eight";
    num[9]="Nine";
    vector<int> num_1;
    vector<string> num_2;
    int i;
    for (i=0;i<arr.size();i++)
    if (arr[i]>=1&&arr[i]<=9)
    num_1.push_back(arr[i]);
    sort(num_1.begin(),num_1.end());
    reverse(num_1.begin(),num_1.end());
    for (i=0;i<num_1.size();i++)
    num_2.push_back(num[num_1[i]]);
    return num_2;
}

