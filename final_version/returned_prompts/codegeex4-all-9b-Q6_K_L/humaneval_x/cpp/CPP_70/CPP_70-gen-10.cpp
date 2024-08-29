    vector<int> a;
    return a;
}
int main()
{
    vector<int> a={1, 2, 3, 4};
    vector<int> b={5, 5, 5, 5};
    vector<int> c={};
    vector<int> d=strange_sort_list(a);
    vector<int> e=strange_sort_list(b);
    vector<int> f=strange_sort_list(c);
    printf("%d %d %d %d %d %d %d %d\n", d.size(), a.size(), b.size(), c.size(), d[0], a[0], b[0], c[0]);
    printf("%d %d %d %d %d %d %d %d\n", e.size(), a.size(), b.size(), c.size(), e[0], a[0], b[0], c[0]);
    printf("%d %d %d %d %d %d %d %d\n", f.size(), a.size(), b.size(), c.size(), f[0], a[0], b[0], c[0]);
    return 0;
}

B:
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> strange_sort_list(vector<int> lst){
    vector<int> a={};
    for(int i=0;i<lst.size();i++)
    {
        if(i%2==0)
        {
            int min=lst[0];
            int min_index=0;
            for(int j=0;j<lst.size();j++)
            {
                if(min>lst[j])
                {
                    min=lst[j];
                    min_index=j;
                }
            }
            a.push_back(min);
            lst[min_index]=INT_MAX;
        }
        else
        {
            int max=lst[0];
            int max_index=0;
            for(int j=0;j<lst.size();j++)
            {
                if(max<lst[j])
                {
                    max=lst[j];
                    max_index=j;
                }
            }
            a.push_back(max);
            lst[max_index]=INT_MIN;
        }
    }
    return a;
}
int main()
{
    vector<int> a={1, 2, 3, 4};
    vector<int> b={5, 5, 5, 5};
    vector<int> c={};
    vector<int> d=strange_sort_list(a);
    vector<int> e=str