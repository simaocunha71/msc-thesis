#include <vector>
#include <string>

using namespace std;

string Strongest_Extension(string class_name, vector<string> extensions)
{
    string strongest = "";
    int max_strength = -1000;
    for (auto extension : extensions)
    {
        int cap = 0;
        int sm = 0;
        for (auto ch : extension)
        {
            if (isupper(ch))
            {
                cap++;
            }
            else if (islower(ch))
            {
                sm++;
            }
        }
        int strength = cap - sm;
        if (strength > max_strength)
        {
            strongest = extension;
            max_strength = strength;
        }
    }
    return class_name + '.' + strongest;
}