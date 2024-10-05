    string result;
    for (int i=0;i<strings.size();i++)
    {
        result+=strings[i];
    }
    return result;
}
// or
#include<string>
#include<vector>
using namespace std;
string concatenate(vector<string> strings){
    string result;
    for (const auto& s : strings)
        result += s;
    return result;
} 

