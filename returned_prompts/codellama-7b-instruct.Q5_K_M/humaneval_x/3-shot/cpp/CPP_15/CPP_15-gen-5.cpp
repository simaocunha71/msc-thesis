    string all_numbers="";
    int i;
    for (i=0;i<=n;i++)
    {
        if (i!=0)
        all_numbers+=" ";
        all_numbers+=to_string(i);
    }
    return all_numbers;
}


