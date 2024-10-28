    string strongest_ext = extensions[0];
    float strongest_strength = count_uppercase(extensions[0])-count_lowercase(extensions[0]);
    for(int i=1; i<extensions.size(); i++){
        float curr_strength = count_uppercase(extensions[i])-count_lowercase(extensions[i]);
        if(curr_strength > strongest_strength){
            strongest_ext = extensions[i];
            strongest_strength = curr_strength;
        }
    }
    return class_name+"."+strongest_ext;
}

int count_uppercase(string s){
    int count=0;
    for(int i=0; i<s.size(); i++){
        if(isupper(s[i])) count++;
    }
    return count;
}

int count_lowercase(string s){
    int count=0;
    for(int i=0; i<s.size(); i++){
        if(islower(s[i])) count++;
    }
    return count;
}


