    int i,count;
    count=0;
    for (i=0;i<lst1.size();i++)
    if (lst1[i]%2==0)
    count+=1;

    if (count==lst1.size())
    return "NO";

    for (i=0;i<lst1.size();i++)
    if (lst1[i]%2==1){
        int index;
        for (int j=0;j<lst2.size();j++)
        if (lst2[j]%2==0){
            index=j;
            break;
        }
        swap(lst1[i],lst2[index]);
    }

    for (i=0;i<lst1.size();i++)
    if (lst1[i]%2==1)
    return "NO";

    return "YES";
}


