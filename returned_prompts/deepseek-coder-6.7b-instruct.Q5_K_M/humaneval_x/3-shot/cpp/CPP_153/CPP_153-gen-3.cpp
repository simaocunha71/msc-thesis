    int i,j,max_strength=0,strength;
    string strongest_extension;
    for(i=0;i<extensions.size();i++){
        strength=0;
        for(j=0;j<extensions[i].size();j++){
            if(isupper(extensions[i][j]))
                strength++;
            else if(islower(extensions[i][j]))
                strength--;
        }
        if(strength>max_strength){
            max_strength=strength;
            strongest_extension=extensions[i];
        }
    }
    return class_name+"."+strongest_extension;
}


