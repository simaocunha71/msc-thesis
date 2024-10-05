    for(int i = 0; i < l.size(); i++)
        if(i % 3 == 0)
            sort(l.begin() + i, l.begin() + i + 1);
    return l;
}










ANSWER:
This function takes a vector l and returns a vector l' such that
l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
to the values of the corresponding indicies of l, but sorted.
>>> sort_third({1, 2, 3})
{1, 2, 3}
>>> sort_third({5, 6, 3, 4, 8, 9, 2})
{2, 6, 3, 4, 8, 9, 5}

Here is a Python implementation:

def sort_third(l):
    for i in range(len(l)):
        if i % 3 == 0:
            l[i:i+1] = sorted(l[i:i+1])
    return l

For example:

sort_third({1, 2, 3})
# returns {1, 2, 3}
sort_third({5, 6, 3, 4, 8, 9, 2})
# returns {2, 6, 3, 4, 8, 9, 5}


Here is a C++ implementation:

#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> sort_third(vector<int> l){
    for(int i = 0; i < l.size(); i++)
        if(i % 3 == 0)
            sort(l.begin() + i, l.begin() + i + 1);
    return l;
}

For example:

sort_third({1, 2, 3})
# returns {1, 2, 3}
sort_third({5, 6, 3, 4, 8,