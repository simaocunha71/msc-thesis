    string strongest_extension = extensions[0];
    int strength = (int)extensions[0].size() - (int)strongest_extension.size();
    for(int i = 1; i < extensions.size(); i++){
        string current_extension = extensions[i];
        int current_strength = (int)extensions[i].size() - (int)current_extension.size();
        if(current_strength > strength){
            strength = current_strength;
            strongest_extension = current_extension;
        }
    }
    return class_name + "." + strongest_extension;
}


