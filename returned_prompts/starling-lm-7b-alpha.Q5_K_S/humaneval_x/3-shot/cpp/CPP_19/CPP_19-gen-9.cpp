    map<string,int> number_map;
    string nums[]={"zero","one","two","three","four","five","six","seven","eight","nine"};
    int i,j;
    for (i=0;i<10;i++)
    number_map[nums[i]]=i;
    string result="";
    string chr;
    char num_chr[5];
    for (i=0;i<numbers.length();i++)
    {
        chr=numbers[i];
        for (j=0;j<5;j++)
        num_chr[j]=chr[j];
        result+=num_chr;
    }
    for (i=0;i<result.length();i++)
    for (j=i+1;j<result.length();j++)
    if (number_map[result[i]]>number_map[result[j]])
    {
        swap(result[i],result[j]);
    }
    return result;
}



