    int max_strength=-1;
    string strongest_extension;
    for (int i=0;i<extensions.size();i++){
        int cap=0;
        int sm=0;
        for (int j=0;j<extensions[i].length();j++){
            if (isupper(extensions[i][j]))
                cap++;
            else
                sm++;
        }
        if (cap-sm>max_strength){
            max_strength=cap-sm;
            strongest_extension=extensions[i];
        }
    }
    return class_name+"."+strongest_extension;
}  // this function is case sensitive. If you want to ignore the case, you should convert both class_name and extensions to lower or upper before comparing them.