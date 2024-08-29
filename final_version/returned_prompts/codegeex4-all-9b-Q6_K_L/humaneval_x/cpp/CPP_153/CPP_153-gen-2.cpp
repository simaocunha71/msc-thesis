#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string Strongest_Extension(string class_name, vector<string> extensions)
{
    int max = -100;
    string str;
    for (int i = 0; i < extensions.size(); i++)
    {
        int temp = 0;
        int count = 0;
        for (int j = 0; j < extensions[i].size(); j++)
        {
            if (extensions[i][j] >= 'A' && extensions[i][j] <= 'Z')
                temp++;
            else if (extensions[i][j] >= 'a' && extensions[i][j] <= 'z')
                count++;
        }
        if (max < (temp - count))
        {
            max = (temp - count);
            str = extensions[i];
        }
    }
    return class_name + "." + str;
}

B:
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    vector<string> ext = {"AA", "Be", "CC"};
    string c = "my_class";
    string res = Strongest_Extension(c, ext);
    cout << res << endl;
    return 0;
}

C:
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

string Strongest_Extension(string class_name, vector<string> extensions)
{
    int max = -100;
    string str;
    for (int i = 0; i < extensions.size(); i++)
    {
        int temp = 0;
        int count = 0;
        for (int j = 0; j < extensions[i].size(); j++)
        {
            if (extensions[i][j] >= 'A' && extensions[i][j] <= 'Z')
                temp++;
            else if (extensions[i][j] >= 'a' && extensions[i][j] <= 'z')
                count++;
        }
        if (max < (temp - count))
        {
            max = (temp - count);
            str = extensions[i];
        }
    }
    return class_name + "." + str;
}

int main()
{
    vector<string> ext = {"AA", "Be", "CC"};
    string c = "my_class";
    string res = Strongest_Extension(c, ext);
    cout << res << endl;
    return 0;
}

D:
#include <iostream>
