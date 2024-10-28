}


//Answer:

#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
string Strongest_Extension(string class_name,vector<string> extensions){
    int max_strength = -1;
    int cur_strength;
    string strongest_ext = "";
    for (int i = 0; i < extensions.size(); i++) {
        cur_strength = 0;
        for (int j = 0; j < extensions[i].size(); j++) {
            if (isupper(extensions[i][j]))
                cur_strength++;
        }
        cur_strength -= count_if(extensions[i].begin(), extensions[i].end(), [](char c) { return islower(c); });
        if (cur_strength > max_strength) {
            max_strength = cur_strength;
            strongest_ext = extensions[i];
        }
    }
    return class_name + "." + strongest_ext;
}


//Test
int main()
{
    vector<string> extensions;
    extensions.push_back("AA");
    extensions.push_back("Be");
    extensions.push_back("CC");
    string class_name = "my_class";
    printf("%s\n", Strongest_Extension(class_name, extensions).c_str());
    return 0;
}