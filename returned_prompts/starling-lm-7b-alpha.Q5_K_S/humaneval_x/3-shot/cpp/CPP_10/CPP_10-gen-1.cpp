    string strcpy=str;
    int i,j;
    for (i=strcpy.size()-1;i>=0;i--)
    {
        for (j=i;j>=0;j--)
        {
            if (strcpy.substr(i,j-i+1)==string(strcpy.substr(i,j-i+1).rbegin(),strcpy.substr(i,j-i+1).rend()))
            {
                strcpy=strcpy.substr(0,i)+string(strcpy.substr(i,j-i+1).rbegin(),strcpy.substr(i,j-i+1).rend())+strcpy.substr(i+1);
                break;
            }
        }
    }
    return strcpy;
}



