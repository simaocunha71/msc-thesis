    string class_name_tmp = class_name;
    string extension_name;
    int cap,sm,max_strength = -1000,strength;
    for(int i = 0;i < extensions.size();i++)
    {
        extension_name = extensions[i];
        cap = 0;
        sm = 0;
        for(int j = 0;j < extension_name.length();j++)
        {
            if(extension_name[j] >= 'A' && extension_name[j] <= 'Z')
                cap++;
            else
                sm++;
        }
        strength = cap - sm;
        if(strength > max_strength)
        {
            max_strength = strength;
            extension_name = extensions[i];
        }
    }
    class_name_tmp += '.' + extension_name;
    return class_name_tmp;
}

int main()
{
    vector<string> extensions = {"SErviNGSliCes","Cheese","StuFfed"};
    printf("%s\n",Strongest_Extension("Slices",extensions).c_str());
    return 0;
}
































*/




























































































































































































