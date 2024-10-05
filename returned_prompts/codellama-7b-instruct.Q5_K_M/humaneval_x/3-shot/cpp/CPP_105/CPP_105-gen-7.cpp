    vector<int> result;
    vector<int> copy_arr;
    map<int, string> number_name;
    number_name[1] = "One";
    number_name[2] = "Two";
    number_name[3] = "Three";
    number_name[4] = "Four";
    number_name[5] = "Five";
    number_name[6] = "Six";
    number_name[7] = "Seven";
    number_name[8] = "Eight";
    number_name[9] = "Nine";
    copy_arr = arr;
    sort(copy_arr.begin(),copy_arr.end());
    for (int i=0;i<copy_arr.size();i++)
    if (copy_arr[i]>0 && copy_arr[i]<10)
    result.push_back(copy_arr[i]);
    sort(result.begin(),result.end());
    reverse(result.begin(),result.end());
    vector<string> answer;
    for (int i=0;i<result.size();i++)
    answer.push_back(number_name[result[i]]);
    return answer;
}


