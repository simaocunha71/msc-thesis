string strongest_extension = extensions[0];
int strongest_strength = 0;
for(int i = 0; i < extensions.size(); i++){
    int cap = 0;
    int sm = 0;
    for(int j = 0; j < extensions[i].size(); j++){
        if(extensions[i][j] >= 'A' && extensions[i][j] <= 'Z')
            cap++;
        else
            sm++;
    }
    int strength = cap - sm;
    if(strength > strongest_strength){
        strongest_strength = strength;
        strongest_extension = extensions[i];
    }
    else if(strength == strongest_strength)
        strongest_extension = extensions[i];
}
return class_name + "." + strongest_extension;
} 

