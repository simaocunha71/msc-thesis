    string strongest_ext="";
    int max_strength=INT_MIN;
    int cap, sm, strength;
    for(string ext: extensions){
        cap=sm=0;
        for(char c: ext){
            if(isupper(c))
                cap++;
            else if(islower(c))
                sm++;
        }
        strength=cap-sm;
        if(strength>max_strength){
            max_strength=strength;
            strongest_ext=ext;
        }
    }
    return class_name+'.'+strongest_ext;
}

