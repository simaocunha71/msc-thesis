    string Strongest_Extension(string class_name,vector<string> extensions){
    string strongest_extension;
    int max_strength=-1;
    for(int i=0;i<extensions.size();i++){
        int strength=(int)extensions[i].size()-(int)(extensions[i].size()-1)*((extensions[i].size()-1)>0);
        if(strength==max_strength){
            if(strongest_extension<extensions[i])
                strongest_extension=extensions[i];
        }
        if(strength>max_strength)
        {
            max_strength=strength;
            strongest_extension=extensions[i];
        }
    }
    return class_name+". "+strongest_extension;
}


























































































































































