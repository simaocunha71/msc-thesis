    int i;
    string strongest;
    int max_strength=-1;
    for (i=0;i<extensions.size();i++)
    {
        int cap=0;
        int sm=0;
        for (int j=0;j<extensions[i].length();j++)
        {
            if (isupper(extensions[i][j]))
                cap++;
            else if (islower(extensions[i][j]))
                sm++;
        }
        if (cap-sm>max_strength)
        {
            max_strength=cap-sm;
            strongest=extensions[i];
        }
    }
    return class_name+"."+strongest;
}
} }  // C++ // C++  // C++ // C++ // C++ // C++ // C++ // C++ // C++  // C++ // C++ // C++ // C++ // C++ // C++ // C++  // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C++ // C