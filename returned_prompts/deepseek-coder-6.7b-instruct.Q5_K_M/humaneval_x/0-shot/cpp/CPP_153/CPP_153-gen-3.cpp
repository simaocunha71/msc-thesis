
    int max_strength = -1000000;
    string strongest_ext = "";
    for(auto ext : extensions){
        int cap = 0, sm = 0;
        for(char c : ext){
            if(isupper(c)) cap++;
            if(islower(c)) sm++;
        }
        int strength = cap - sm;
        if(strength > max_strength){
            max_strength = strength;
            strongest_ext = ext;
        }
    }
    return class_name+"."+strongest_ext;
}

int main(){
    string className = "my_class";
    vector<string> extensions = {"AA", "Be", "CC"};
    printf("%s",Strongest_Extension(className, extensions).c_str());
    return 0;
}

*/

int main(){
    string className = "my_class";
    vector<string> extensions = {"AA", "Be", "CC"};
    printf("%s",Strongest_Extension(className, extensions).c_str());
    return 0;
}

*/

int main(){
    string className = "my_class";
    vector<string> extensions = {"AA", "Be", "CC"};
    printf("%s",Strongest_Extension(className, extensions).c_str());
    return 0;
}

*/

int main(){
    string className = "my_class";
    vector<string> extensions = {"AA", "Be", "CC"};
    printf("%s",Strongest_Extension(className, extensions).c_str());
    return 0;
}

*/

int main(){
    string className = "my_class";
    vector<string> extensions = {"AA", "Be", "CC"};
    printf("%s",Strongest_Extension(className, extensions).c_str());
    return 0;
}

*/

int main(){
    string className = "my_class";
    vector<string> extensions = {"AA", "Be", "CC"};
    printf("%s",Strongest_Extension(className, extensions).c