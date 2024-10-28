    for(int i = 0; i < extensions.size(); i++)
    {
        string extension = extensions[i];
        int count_upper = 0;
        int count_lower = 0;
        for(int j = 0; j < extension.size(); j++)
        {
            if(isupper(extension[j]))
            {
                count_upper++;
            }
            else
            {
                count_lower++;
            }
        }
        double strength = (double)count_upper / count_lower;
        if(i == 0)
        {
            double strongest_strength = strength;
            string strongest_extension = extension;
            goto A;
        }
        if(strength > strongest_strength)
        {
            strongest_strength = strength;
            strongest_extension = extension;
        }
    }
    return class_name + "." + strongest_extension;
}
