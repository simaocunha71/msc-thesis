#include <iostream>
#include <vector>
#include <string>
using namespace std;

string match_parens(vector<string> lst)
{
    vector<char> s;
    for (int i=0; i<lst.size(); ++i)
    {
        for (int j=0; j<lst[i].size(); ++j)
        {
            s.push_back(lst[i][j]);
        }
    }
    int cnt = 0;
    for (int i=0; i<s.size(); ++i)
    {
        if (s[i] == '(') cnt++;
        else cnt--;
        if (cnt < 0) return "No";
    }
    if (cnt == 0) return "Yes";
    else return "No";
}
int main()
{
    vector<string> v;
    v.push_back("()(");
    v.push_back(")");
    cout << match_parens(v) << endl;
    return 0;
}

B:
#include <iostream>
#include <vector>
#include <string>
using namespace std;

string match_parens(vector<string> lst)
{
    int cnt = 0;
    for (int i=0; i<lst.size(); ++i)
    {
        for (int j=0; j<lst[i].size(); ++j)
        {
            if (lst[i][j] == '(') cnt++;
            else cnt--;
        }
    }
    if (cnt == 0) return "Yes";
    else return "No";
}
int main()
{
    vector<string> v;
    v.push_back("()(");
    v.push_back(")");
    cout << match_parens(v) << endl;
    return 0;
}

C:
#include <iostream>
#include <vector>
#include <string>
using namespace std;

string match_parens(vector<string> lst)
{
    vector<char> s;
    for (int i=0; i<lst.size(); ++i)
    {
        for (int j=0; j<lst[i].size(); ++j)
        {
            s.push_back(lst[i][j]);
        }
    }
    int cnt = 0;
    for (int i=0; i<s.size(); ++i)
    {
        if (s[i] == '(') cnt++;
        else cnt--;
        if (cnt < 0) return "No";
    }
    if (cnt == 0) return "Yes";
    else return "No";
}
