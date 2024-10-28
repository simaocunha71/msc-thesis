    int i,j;
    for (i=0;i<a.length();i++)
    {
        bool found=true;
        for (j=0;j<b.length();j++)
        {
            if (a[(i+j)%a.length()]!=b[j])
            {
                found=false;
                break;
            }
        }
        if (found)
        return true;
    }
    return false;
}


