    int max_strength = 0;
    string strongest_extension;
    for(auto &extension : extensions){
        int cap = 0;
        int sm = 0;
        for(auto &c : extension){
            if(isupper(c)) cap++;
            else if(islower(c)) sm++;
        }
        int strength = cap - sm;
        if(strength > max_strength){
            max_strength = strength;
            strongest_extension = extension;
        }
    }
    return class_name + "." + strongest_extension;
}

B:
    int max_strength = 0;
    string strongest_extension;
    for(auto &extension : extensions){
        int cap = 0;
        int sm = 0;
        for(auto &c : extension){
            if(isupper(c)) cap++;
            else if(islower(c)) sm++;
        }
        int strength = cap - sm;
        if(strength >= max_strength){
            max_strength = strength;
            strongest_extension = extension;
        }
    }
    return class_name + "." + strongest_extension;
}

C:
    int max_strength = 0;
    string strongest_extension;
    for(auto &extension : extensions){
        int cap = 0;
        int sm = 0;
        for(auto &c : extension){
            if(isupper(c)) cap++;
            else if(islower(c)) sm++;
        }
        int strength = cap - sm;
        if(strength > max_strength){
            max_strength = strength;
            strongest_extension = extension;
        }
        else if(strength == max_strength){
            if(extension < strongest_extension) strongest_extension = extension;
        }
    }
    return class_name + "." + strongest_extension;
}

D:
    int max_strength = 0;
    string strongest_extension;
    for(auto &extension : extensions){
        int cap = 0;
        int sm = 0;
        for(auto &c : extension){
            if(isupper(c)) cap++;
            else if(islower(c)) sm++;
        }
        int strength = cap - sm;
        if(strength >= max_strength){
            max_strength = strength;
            strongest_extension = extension;
        }
    }
    return class_name + "." + strongest_extension;
}

E:
    int max_strength = 0;
    string strongest_extension;
    for(auto &extension : extensions){
        int cap = 0;
        int sm = 0;
        for(auto &c : extension){
            if(isupper(c)) cap++;
            else if(islower(c)) sm++;
       