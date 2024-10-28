    bool is_even=true;
    for (int i=0;i<lst1.size();i++)
    if (lst1[i]%2==1){
        is_even=false;
        break;
    }
    if (is_even){
        return "YES";
    }

    is_even=true;
    for (int i=0;i<lst2.size();i++)
    if (lst2[i]%2==1){
        is_even=false;
        break;
    }
    if (is_even){
        return "YES";
    }

    for (int i=0;i<lst1.size();i++)
    for (int j=0;j<lst2.size();j++)
    if (lst1[i]==lst2[j]){
        lst1[i]=lst2[j]=0;
        break;
    }
    is_even=true;
    for (int i=0;i<lst1.size();i++)
    if (lst1[i]%2==1){
        is_even=false;
        break;
    }
    if (is_even){
        return "YES";
    }
    return "NO";
}


