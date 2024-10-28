    int strongest_score = 0;
    string strongest_extension_name = "";
    for(int i = 0; i < extensions.size(); i++){
        string extension = extensions[i];
        int cap = 0;
        int sm = 0;
        for(int j = 0; j < extension.size(); j++){
            if(extension[j] >= 'A' && extension[j] <= 'Z'){
                cap++;
            } else {
                sm++;
            }
        }
        int score = cap - sm;
        if(score > strongest_score){
            strongest_score = score;
            strongest_extension_name = extension;
        } else if(score == strongest_score && j > i){
            strongest_extension_name = extension;
        }
    }
    return class_name + "." + strongest_extension_name;
}
