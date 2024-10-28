    int i,j;
    for (i=0;i<lst1.size();i++)
    if (lst1[i]%2==1){
        for (j=0;j<lst2.size();j++)
        if (lst2[j]%2==1){
            lst1[i]=lst2[j];
            lst2[j]=lst1[i];
            break;
        }
        if (lst2[j]%2==0)
        return "NO";
    }
    return "YES";
}



