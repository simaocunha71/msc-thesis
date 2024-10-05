    map<string,int> map_num;
    string nums[10]={"zero","one","two","three","four","five","six","seven","eight","nine"};
    int i;
    for (i=0;i<10;i++)
    map_num[nums[i]]=i;
    string sorted_nums[10];
    for (i=0;i<numbers.length();i++)
    sorted_nums[i]=numbers[i];
    for (i=0;i<numbers.length();i++)
    for (int j=i+1;j<numbers.length();j++)
    if (map_num[sorted_nums[i]]>map_num[sorted_nums[j]])
    {
    string temp=sorted_nums[i];
    sorted_nums[i]=sorted_nums[j];
    sorted_nums[j]=temp;
    }
    string sorted_str;
    for (i=0;i<numbers.length();i++)
    sorted_str+=sorted_nums[i];
    return sorted_str;
}


