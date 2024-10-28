    bool check=true;
    int i;
    for (i=1;i<lst.size();i++)
    if (lst[i]<lst[i-1])
    {
        check=false;
        break;
    }

    return check;
}


