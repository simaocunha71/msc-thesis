    int max_strength=-9999999;
    string strongest_extension;
    for(string extension:extensions){
        int cap=0,sm=0;
        for(char c:extension){
            if(isupper(c)) cap++;
            else if(islower(c)) sm++;
        }
        int strength=cap-sm;
        if(strength>max_strength){
            max_strength=strength;
            strongest_extension=extension;
        }
    }
    return class_name+"."+strongest_extension;

B:
    int max_strength = -9999999;
    string strongest_extension = "";
    for (string extension : extensions) {
        int cap = 0, sm = 0;
        for (char c : extension) {
            if (isupper(c)) cap++;
            else if (islower(c)) sm++;
        }
        int strength = cap - sm;
        if (strength > max_strength) {
            max_strength = strength;
            strongest_extension = extension;
        }
    }
    return class_name + "." + strongest_extension;

C:
    int max_strength = -9999999;
    string strongest_extension = "";
    for (string extension : extensions) {
        int cap = 0, sm = 0;
        for (char c : extension) {
            if (isupper(c)) cap++;
            else if (islower(c)) sm++;
        }
        int strength = cap - sm;
        if (strength > max_strength) {
            max_strength = strength;
            strongest_extension = extension;
        }
    }
    return class_name + "." + strongest_extension;

D:
    int max_strength = -9999999;
    string strongest_extension = "";
    for (string extension : extensions) {
        int cap = 0, sm = 0;
        for (char c : extension) {
            if (isupper(c)) cap++;
            else if (islower(c)) sm++;
        }
        int strength = cap - sm;
        if (strength > max_strength) {
            max_strength = strength;
            strongest_extension = extension;
        }
    }
    return class_name + "." + strongest_extension;

E:
    int max_strength = -9999999;
    string strongest_extension = "";
    for (string extension : extensions) {
        int cap = 0, sm = 0;
        for (char c : extension) {
            if (isupper(c)) cap++;
            else if (islower(c)) sm++;
        }
        int strength = cap - sm;
       