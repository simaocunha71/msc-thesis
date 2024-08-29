#include <bits/stdc++.h>
using namespace std;
vector<int> f(int n)
{
    vector<int> res(n);
    for (int i = 0; i < n; i++)
    {
        if (i % 2 == 0)
        {
            res[i] = 1;
            for (int j = 2; j <= i; j++)
            {
                res[i] *= j;
            }
        }
        else
        {
            res[i] = i;
            for (int j = 1; j < i; j++)
            {
                res[i] += j;
            }
        }
    }
    return res;
}
B:
#include <bits/stdc++.h>
using namespace std;
vector<int> f(int n)
{
    vector<int> res(n);
    for (int i = 0; i < n; i++)
    {
        if (i % 2 == 0)
        {
            res[i] = 1;
            for (int j = 2; j <= i; j++)
            {
                res[i] *= j;
            }
        }
        else
        {
            res[i] = i;
            for (int j = 1; j < i; j++)
            {
                res[i] += j;
            }
        }
    }
    return res;
}
C:
#include <bits/stdc++.h>
using namespace std;
vector<int> f(int n)
{
    vector<int> res(n);
    for (int i = 0; i < n; i++)
    {
        if (i % 2 == 0)
        {
            res[i] = 1;
            for (int j = 2; j <= i; j++)
            {
                res[i] *= j;
            }
        }
        else
        {
            res[i] = i;
            for (int j = 1; j < i; j++)
            {
                res[i] += j;
            }
        }
    }
    return res;
}
D:
#include <bits/stdc++.h>
using namespace std;
vector<int> f(int n)
{
    vector<int> res(n);
    for (int i = 0; i < n; i++)
    {
        if (i % 2 == 0)
        {
            res[i] = 1;
            for (int j = 2; j <= i; j++)
            {
                res[i] *= j;
           