    int i,j;
    bool is_found=false;
    for (i=0;i<a.length();i++)
    {
        j=i;
        while (j<a.length())
        {
            if (a.substr(j,b.length())==b)
            {
                is_found=true;
                break;
            }
            j++;
        }
        if (is_found)
        break;
    }
    return is_found;
}




