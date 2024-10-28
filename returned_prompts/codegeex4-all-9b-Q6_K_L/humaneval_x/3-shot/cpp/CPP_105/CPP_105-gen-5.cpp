    vector<int> sort_arr(arr);
    sort(sort_arr.begin(),sort_arr.end());
    vector<int> rev_arr(sort_arr);
    reverse(rev_arr.begin(),rev_arr.end());
    vector<string> final_arr;
    map<int,string> digit;
    digit[1]="One";
    digit[2]="Two";
    digit[3]="Three";
    digit[4]="Four";
    digit[5]="Five";
    digit[6]="Six";
    digit[7]="Seven";
    digit[8]="Eight";
    digit[9]="Nine";
    for (int i=0;i<rev_arr.size();i++)
    {
        if (rev_arr[i]>0&&rev_arr[i]<10)
        final_arr.push_back(digit[rev_arr[i]]);
    }
    return final_arr;
}

