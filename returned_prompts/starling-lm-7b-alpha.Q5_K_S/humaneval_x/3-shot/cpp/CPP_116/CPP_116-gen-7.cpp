    vector<int> temp;
    int i,j;
    int one_count;
    int max_one_count=0;
    for (i=0;i<arr.size();i++)
    {
        one_count=0;
        j=arr[i];
        while (j>0){
        one_count+=j%2;
        j/=2;
        }
        if (one_count>max_one_count){
        max_one_count=one_count;
        temp.clear();
        temp.push_back(arr[i]);
        }
        else if (one_count==max_one_count){
        temp.push_back(arr[i]);
        }
    }
    sort(temp.begin(),temp.end());
    return temp;
}


