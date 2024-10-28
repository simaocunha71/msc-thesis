    int odd_lst1=0, even_lst2=0;
    for(int i=0;i<lst1.size();i++)
        if(lst1[i]%2)
            odd_lst1++;
    for(int i=0;i<lst2.size();i++)
        if(!(lst2[i]%2))
            even_lst2++;
    if(odd_lst1>even_lst2)
        return "NO";
    else
        return "YES";
}


