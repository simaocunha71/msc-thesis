    int strongest_extension_index = 0;
    int strongest_extension_strength = 0;
    for(int i = 0; i < extensions.size(); i++){
        int cap = 0;
        int sm = 0;
        for(int j = 0; j < extensions[i].size(); j++){
            if(extensions[i][j] >= 'A' && extensions[i][j] <= 'Z'){
                cap++;
            }else if(extensions[i][j] >= 'a' && extensions[i][j] <= 'z'){
                sm++;
            }
        }
        int extension_strength = cap - sm;
        if(extension_strength > strongest_extension_strength){
            strongest_extension_index = i;
            strongest_extension_strength = extension_strength;
        }
    }
    return class_name + "." + extensions[strongest_extension_index];
}
int main(){
    cout << Strongest_Extension("Slices", {"SErviNGSliCes", "Cheese", "StuFfed"}) << endl;
    return 0;
}

