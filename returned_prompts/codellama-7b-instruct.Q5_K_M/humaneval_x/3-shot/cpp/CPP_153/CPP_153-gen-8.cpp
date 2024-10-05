    int strongest_strength=0;
    int strength=0;
    int i;
    string strongest_extension;
    for (i=0;i<extensions.size();i++){
        strength=0;
        strength+=extensions[i].length();
        strength-=extensions[i].size();
        if (strength>strongest_strength)
        {
            strongest_strength=strength;
            strongest_extension=extensions[i];
        }
    }
    return class_name+"."+strongest_extension;
}



