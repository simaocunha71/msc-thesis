    int i,j;
    bool flag=true;
    for (i=0;i<arr.size()-1;i++)
    for (j=i+1;j<arr.size();j++)
    if (arr[i]>arr[j])
    {
        flag=false;
        break;
    }
    return flag;
}



