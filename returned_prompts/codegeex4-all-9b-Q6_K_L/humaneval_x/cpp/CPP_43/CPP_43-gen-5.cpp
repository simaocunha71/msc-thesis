#include <stdio.h>
#include <string.h>
#include <vector>
using namespace std;

bool pairs_sum_to_zero(vector<int> l)
{
    for (int i = 0; i < l.size(); i++)
    {
        for (int j = i + 1; j < l.size(); j++)
        {
            if (l[i] + l[j] == 0)
                return true;
        }
    }
    return false;
}

int main()
{
    vector<int> l = {1, 3, 5, 0};
    printf("%d\n", pairs_sum_to_zero(l));

    l = {1, 3, -2, 1};
    printf("%d\n", pairs_sum_to_zero(l));

    l = {1, 2, 3, 7};
    printf("%d\n", pairs_sum_to_zero(l));

    l = {2, 4, -5, 3, 5, 7};
    printf("%d\n", pairs_sum_to_zero(l));

    l = {1};
    printf("%d\n", pairs_sum_to_zero(l));

    return 0;
}

C:
#include <stdio.h>
#include <string.h>
#include <vector>
using namespace std;

bool pairs_sum_to_zero(vector<int> l)
{
    for (int i = 0; i < l.size(); i++)
    {
        for (int j = i + 1; j < l.size(); j++)
        {
            if (l[i] + l[j] == 0)
                return true;
        }
    }
    return false;
}

int main()
{
    vector<int> l = {1, 3, 5, 0};
    printf("%d\n", pairs_sum_to_zero(l));

    l = {1, 3, -2, 1};
    printf("%d\n", pairs_sum_to_zero(l));

    l = {1, 2, 3, 7};
    printf("%d\n", pairs_sum_to_zero(l));

    l = {2, 4, -5, 3, 5, 7};
    printf("%d\n", pairs_sum_to_zero(l));

    l = {1};
    printf("%d\n", pairs_sum_to_zero(l));

    return 0;
}

D:
#include<stdio.h>
#include<vector>
using namespace std;
bool pairs_sum_to_zero(vector<int> l){

    for(int i = 0; i