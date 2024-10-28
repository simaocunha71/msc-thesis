    int i;
    int j;
    for (i=0;i<lst1.size();i++)
    for (j=0;j<lst2.size();j++)
    if (lst1[i]%2==0 && lst2[j]%2!=0){
        lst2[j]=lst1[i];
        lst1[i]=0;
        break;
    }
    string result="NO";
    for (i=0;i<lst1.size();i++)
    if (lst1[i]!=0)
    result="YES";
    return result;
}


