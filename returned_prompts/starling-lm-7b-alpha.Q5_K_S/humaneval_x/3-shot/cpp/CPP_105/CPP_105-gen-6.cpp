    vector<int> arr_cp = arr;
    sort(arr_cp.begin(), arr_cp.end());
    vector<string> result;
    for (int i=0;i<arr.size();i++)
    {
        if (arr_cp[i]>=1 && arr_cp[i]<=9)
        result.push_back(to_string(arr_cp[i]));
    }
    sort(result.begin(), result.end());
    reverse(result.begin(), result.end());
    for (int i=0;i<result.size();i++)
    {
        if (result[i]=="1")
        result[i]="One";
        if (result[i]=="2")
        result[i]="Two";
        if (result[i]=="3")
        result[i]="Three";
        if (result[i]=="4")
        result[i]="Four";
        if (result[i]=="5")
        result[i]="Five";
        if (result[i]=="6")
        result[i]="Six";
        if (result[i]=="7")
        result[i]="Seven";
        if (result[i]=="8")
        result[i]="Eight";
        if (result[i]=="9")
        result[i]="Nine";
    }
    return result;
}


