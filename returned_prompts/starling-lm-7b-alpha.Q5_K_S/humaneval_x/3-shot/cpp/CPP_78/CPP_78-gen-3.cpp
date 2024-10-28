    int i,j;
    int count=0;
    string hex_list="0123456789ABCDEF";
    for (i=0;i<num.length();i++)
    {
        j=hex_list.find(num[i]);
        if (j==2||j==3||j==5||j==7||j==11||j==13)
        count+=1;
    }
    return count;
}



