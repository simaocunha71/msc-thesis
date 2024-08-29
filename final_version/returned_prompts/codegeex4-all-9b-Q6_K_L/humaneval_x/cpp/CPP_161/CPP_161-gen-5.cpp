#include <bits/stdc++.h>
#include <string>
using namespace std;
string solve(string s)
{
    string a = "";
    for (int i = 0; i < s.length(); i++)
    {
        if (isalpha(s[i]))
        {
            if (islower(s[i]))
            {
                a += toupper(s[i]);
            }
            else
            {
                a += tolower(s[i]);
            }
        }
        else
        {
            a += s[i];
        }
    }
    reverse(a.begin(), a.end());
    return a;
}

B:
#include <bits/stdc++.h>
#include <string>
using namespace std;
string solve(string s)
{
    string a = "";
    for (int i = 0; i < s.length(); i++)
    {
        if (isalpha(s[i]))
        {
            if (islower(s[i]))
            {
                a += toupper(s[i]);
            }
            else
            {
                a += tolower(s[i]);
            }
        }
        else
        {
            a += s[i];
        }
    }
    return a;
}

C:
#include<bits/stdc++.h>
using namespace std;
string solve(string s)
{
    string a = "";
    for (int i = 0; i < s.length(); i++)
    {
        if (isalpha(s[i]))
        {
            if (islower(s[i]))
            {
                a += toupper(s[i]);
            }
            else
            {
                a += tolower(s[i]);
            }
        }
        else
        {
            a += s[i];
        }
    }
    return a;
}

D:
#include<bits/stdc++.h>
#include <string>
using namespace std;
string solve(string s)
{
    string a = "";
    for (int i = 0; i < s.length(); i++)
    {
        if (isalpha(s[i]))
        {
            if (islower(s[i]))
            {
                a += toupper(s[i]);
            }
            else
            {
                a += tolower(s[i]);
            }
        }
        else
        {
            a += s[i];
        }
    }
    return a;
}
E:
#include<bits/stdc++.h>
#include <string>
using namespace std;
string solve(string s)
{
    string a = "";
    for (int i = 0; i < s.length(); i++)
    {
        if (isalpha(s[i]))
        {
            if (islower