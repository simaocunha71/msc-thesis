    int i,j;
    int total=0;
    int len_substring=substring.length();
    int len_str=str.length();
    for (i=0;i<len_str;i++)
    {
        for (j=0;j<len_substring;j++)
        if (str[i+j]!=substring[j])
        break;
        if (j==len_substring){
        total+=1;
        i+=j;
        }
    }
    return total;
}



