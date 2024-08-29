#include <stdio.h>
#include <vector>
using namespace std;

double double_the_difference(vector<float> lst)
{
    double sum = 0;
    for (int i = 0; i < lst.size(); i++)
    {
        if (lst[i] > 0 && (int)lst[i] == lst[i] && lst[i] % 2 != 0)
        {
            sum += pow(lst[i], 2);
        }
    }
    return sum;
}
B:
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
long long double_the_difference(vector<float> lst){

C:
#include <stdio.h>
#include <vector>
using namespace std;

double double_the_difference(vector<float> lst)
{
    double sum = 0;
    for (int i = 0; i < lst.size(); i++)
    {
        if (lst[i] > 0 && (int)lst[i] == lst[i] && lst[i] % 2 != 0)
        {
            sum += pow(lst[i], 2);
        }
    }
    return sum;
}