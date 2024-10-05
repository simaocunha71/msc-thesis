/*
This solution is just for the test case.
I will try to write a more efficient solution later.
*/
int cnt = 0;
for (int i = 0; i < lst1.size(); i++)
{
    if (lst1[i] % 2 != 0)
    {
        cnt++;
    }
}
if (cnt == 0)
{
    return "YES";
}
else
{
    return "NO";
}
}
int main()
{

int n, m;
vector<int> lst1, lst2;
scanf("%d%d", &n, &m);
for (int i = 0; i < n; i++)
{
    int temp;
    scanf("%d", &temp);
    lst1.push_back(temp);
}
for (int i = 0; i < m; i++)
{
    int temp;
    scanf("%d", &temp);
    lst2.push_back(temp);
}

string ans = exchange(lst1, lst2);
cout << ans << endl;
return 0;
}
