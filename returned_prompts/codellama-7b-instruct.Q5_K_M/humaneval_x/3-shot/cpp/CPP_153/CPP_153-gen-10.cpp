    int strength=-1,temp;
    string strongest_extension;
    for (int i=0;i<extensions.size();i++)
    {
        temp=0;
        for (int j=0;j<extensions[i].length();j++)
        {
            if (isupper(extensions[i][j]))
            temp++;
        }
        if (temp>strength)
        {
            strength=temp;
            strongest_extension=extensions[i];
        }
    }
    return class_name+"."+strongest_extension;
}



