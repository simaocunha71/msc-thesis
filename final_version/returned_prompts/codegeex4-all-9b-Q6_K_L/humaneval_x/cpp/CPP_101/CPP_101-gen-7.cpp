#include <vector>
#include <string>

using namespace std;

vector<string> words_string(string s)
{
    vector<string> result;
    size_t pos = 0;
    size_t pos2 = 0;

    while (true)
    {
        pos = s.find_first_not_of(" ,", pos2);
        if (pos == string::npos)
        {
            break;
        }
        pos2 = s.find_first_of(" ,", pos);
        if (pos2 == string::npos)
        {
            pos2 = s.size();
        }
        result.push_back(s.substr(pos, pos2 - pos));
    }

    return result;
}

B:
#include <vector>
#include <string>

using namespace std;

vector<string> words_string(string s)
{
    vector<string> result;
    size_t pos = 0;
    size_t pos2 = 0;

    while (true)
    {
        pos = s.find_first_not_of(" ,", pos2);
        if (pos == string::npos)
        {
            break;
        }
        pos2 = s.find_first_of(" ,", pos);
        if (pos2 == string::npos)
        {
            pos2 = s.size();
        }
        result.push_back(s.substr(pos, pos2 - pos));
    }

    return result;
}

C:
#include <vector>
#include <string>

using namespace std;

vector<string> words_string(string s)
{
    vector<string> result;
    size_t pos = 0;
    size_t pos2 = 0;

    while (true)
    {
        pos = s.find_first_not_of(" ,", pos2);
        if (pos == string::npos)
        {
            break;
        }
        pos2 = s.find_first_of(" ,", pos);
        if (pos2 == string::npos)
        {
            pos2 = s.size();
        }
        result.push_back(s.substr(pos, pos2 - pos));
    }

    return result;
}

D:
#include <vector>
#include <string>

using namespace std;

vector<string> words_string(string s)
{
    vector<string> result;
    size_t pos = 0;
    size_t pos2 = 0;

    while (true)
    {
        pos = s.find_first_not_of(" ,", pos2);
        if (pos == string::npos)
        {
            break;
        }
        pos2 = s.find_first_of(" ,", pos);
        if (pos2 == string