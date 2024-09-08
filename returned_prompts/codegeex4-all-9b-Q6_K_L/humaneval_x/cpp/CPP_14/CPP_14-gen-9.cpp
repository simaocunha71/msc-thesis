#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<string> all_prefixes(string str)
{
    vector<string> prefixes;
    for (int i = 0; i < str.length(); i++)
    {
        prefixes.push_back(str.substr(0, i + 1));
    }
    return prefixes;
}

int main()
{
    vector<string> prefixes = all_prefixes("abc");
    for (string prefix : prefixes)
    {
        cout << prefix << endl;
    }
    return 0;
}

B:
#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<string> all_prefixes(string str)
{
    vector<string> prefixes;
    for (int i = 0; i < str.length(); i++)
    {
        string prefix = str.substr(0, i + 1);
        prefixes.push_back(prefix);
    }
    return prefixes;
}

int main()
{
    vector<string> prefixes = all_prefixes("abc");
    for (string prefix : prefixes)
    {
        cout << prefix << endl;
    }
    return 0;
}

C:
#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<string> all_prefixes(string str)
{
    vector<string> prefixes;
    for (int i = 0; i < str.length(); i++)
    {
        prefixes.push_back(str.substr(i, str.length() - i));
    }
    return prefixes;
}

int main()
{
    vector<string> prefixes = all_prefixes("abc");
    for (string prefix : prefixes)
    {
        cout << prefix << endl;
    }
    return 0;
}

D:
#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<string> all_prefixes(string str)
{
    vector<string> prefixes;
    for (int i = 1; i <= str.length(); i++)
    {
        prefixes.push_back(str.substr(0, i));
    }
    return prefixes;
}

int main()
{
    vector<string> prefixes = all_prefixes("abc");
    for (string prefix : prefixes)
    {
        cout << prefix << endl;
    }
    return 0;
}

E:
#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<string> all_prefixes(string str)
{
    vector<string> prefixes;
    for (int i = 0; i < str.length(); i++)
    {
        prefixes.push