    int i = 0, j = 0, k = 0, n = extensions.size();
    string s1, s2, s3, s4, s5;
    int num1 = 0, num2 = 0;
    double num3 = 0, num4 = 0;
    while (i < class_name.size())
    {
        if (class_name[i] >= 'A' && class_name[i] <= 'Z')
            num1++;
        i++;
    }
    i = 0;
    while (i < class_name.size())
    {
        if (class_name[i] >= 'a' && class_name[i] <= 'z')
            num2++;
        i++;
    }
    double strength = (num1 - num2) / double(num1 + num2);
    while (k < n)
    {
        int num5 = 0, num6 = 0;
        double num7 = 0;
        s1 = extensions[k];
        i = 0;
        while (i < s1.size())
        {
            if (s1[i] >= 'A' && s1[i] <= 'Z')
                num5++;
            i++;
        }
        i = 0;
        while (i < s1.size())
        {
            if (s1[i] >= 'a' && s1[i] <= 'z')
                num6++;
            i++;
        }
        num7 = (num5 - num6) / double(num5 + num6);
        if (num7 > strength)
        {
            strength = num7;
            s2 = s1;
        }
        k++;
    }
    s3 = class_name;
    s3.append(".");
    s3.append(s2);
    return s3;
}

























































