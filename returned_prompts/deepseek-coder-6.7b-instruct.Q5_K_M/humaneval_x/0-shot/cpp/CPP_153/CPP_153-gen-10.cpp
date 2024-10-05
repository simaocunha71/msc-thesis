    int n = extensions.size();
    int max_strength = -1000000;
    string strongest_extension = "";
    for(int i=0; i<n; i++){
        int cap = 0, sm = 0;
        for(int j=0; j<extensions[i].size(); j++){
            if(isupper(extensions[i][j])) cap++;
            else if(islower(extensions[i][j])) sm++;
        }
        int strength = cap - sm;
        if(strength>max_strength){
            max_strength = strength;
            strongest_extension = extensions[i];
        }
    }
    return class_name+"."+strongest_extension;
}

int main(){
    vector<string> v = {"AA", "Be", "CC"};
    printf(Strongest_Extension("my_class",v).c_str());
    return 0;
}

*/

#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string Strongest_Extension(string class_name,vector<string> extensions){

    int n = extensions.size();
    int max_strength = -1000000;
    string strongest_extension = "";
    for(int i=0; i<n; i++){
        int cap = 0, sm = 0;
        for(int j=0; j<extensions[i].size(); j++){
            if(isupper(extensions[i][j])) cap++;
            else if(islower(extensions[i][j])) sm++;
        }
        int strength = cap - sm;
        if(strength>max_strength){
            max_strength = strength;
            strongest_extension = extensions[i];
        }
    }
    return class_name+"."+strongest_extension;
}

int main(){
    vector<string> v = {"AA", "Be", "CC"};
    printf(Strongest_Extension("my_class",v).c_str());
    return 0;
}

