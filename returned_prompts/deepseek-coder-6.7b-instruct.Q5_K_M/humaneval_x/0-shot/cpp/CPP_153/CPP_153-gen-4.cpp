    int max = -1000000;
    string result;
    for(int i=0;i<extensions.size();i++){
        int cap = 0, sm = 0;
        for(int j=0;j<extensions[i].length();j++){
            if(isupper(extensions[i][j]))
                cap++;
            else if(islower(extensions[i][j]))
                sm++;
        }
        if(cap - sm > max){
            max = cap - sm;
            result = class_name + "." + extensions[i];
        }
    }
    return result;
}

main(){
    vector<string> ext = {"AA", "Be", "CC"};
    printf("%s", Strongest_Extension("my_class", ext).c_str());
    return 0;
}

This code will calculate the strength of each extension and compare it with the current max. If the extension's strength is greater, then it will update the max and save the extension's name. Finally, it will return the class name along with the strongest extension.
*/

*/

#include<iostream>
#include<vector>
#include<string>
using namespace std;

string Strongest_Extension(string class_name,vector<string> extensions){

    int max = -1000000;
    string result;
    for(int i=0;i<extensions.size();i++){
        int cap = 0, sm = 0;
        for(int j=0;j<extensions[i].length();j++){
            if(isupper(extensions[i][j]))
                cap++;
            else if(islower(extensions[i][j]))
                sm++;
        }
        if(cap - sm > max){
            max = cap - sm;
            result = class_name + "." + extensions[i];
        }
    }
    return result;
}

int main(){
    vector<string> ext = {"AA", "Be", "CC"};
    cout << Strongest_Extension("my_class", ext);
    return 0;
}
