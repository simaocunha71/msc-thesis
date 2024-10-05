    int i;
    int max_strength=0;
    int current_strength=0;
    string max_extension="";
    string current_extension="";
    for (i=0;i<extensions.size();i++){
        current_extension=extensions[i];
        current_strength=0;
        for (j=0;j<current_extension.length();j++){
            if (isupper(current_extension[j]))
            current_strength+=1;
        }
        current_strength-=current_extension.length();
        if (current_strength>max_strength){
            max_strength=current_strength;
            max_extension=current_extension;
        }
    }
    return class_name+"."+max_extension;
}



