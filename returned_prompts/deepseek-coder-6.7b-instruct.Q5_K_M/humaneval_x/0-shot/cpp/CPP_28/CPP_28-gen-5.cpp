    string result;
    for (int i = 0; i < strings.size(); i++){
        result += strings[i];
    }
    return result;
}

int main(){
    vector<string> test1;
    printf("%s\n", concatenate(test1).c_str());
    vector<string> test2 = {"a", "b", "c"};
    printf("%s\n", concatenate(test2).c_str());
}


A: You can use the accumulate function from the STL algorithm library which is a more elegant solution.

Code:

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

string concatenate(vector<string> strings){
    return accumulate(strings.begin(), strings.end(), string(""));
}

int main(){
    vector<string> test1;
    cout << concatenate(test1) << endl;
    vector<string> test2 = {"a", "b", "c"};
    cout << concatenate(test2) << endl;
}

The function accumulate(strings.begin(), strings