    int i,j;
    int best_strength=0;
    string best_name="";
    int current_strength;
    string current_name;
    for (i=0;i<extensions.size();i++)
    {
        current_name=extensions[i];
        current_strength=0;
        for (j=0;j<current_name.length();j++)
        if (current_name[j]>='A' && current_name[j]<='Z')
        current_strength+=current_name[j]-'A'+1;
        else if (current_name[j]>='a' && current_name[j]<='z')
        current_strength-=current_name[j]-'a';
        if (current_strength>best_strength)
        {
            best_strength=current_strength;
            best_name=current_name;
        }
        if (current_strength==best_strength)
        if (extensions[i]<best_name)
        {
            best_strength=current_strength;
            best_name=current_name;
        }
    }
    return class_name+"."+best_name;
}



