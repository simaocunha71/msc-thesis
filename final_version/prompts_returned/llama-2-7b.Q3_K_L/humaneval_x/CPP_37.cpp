/*
This function takes a vector l and returns a vector l' such that
l' is identical to l in the odd indicies, while its values at the even indicies are equal
to the values of the even indicies of l, but sorted.
>>> sort_even({1, 2, 3})
{1, 2, 3}
>>> sort_even({5, 6, 3, 4})
{3, 6, 5, 4}
*/
#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<float> sort_even(vector<float> l){
	int size = l.size();
	if (size % 2 != 1) return l;
	sort(l.begin(), l.end());
	swap(l[0], l[size-1]);
	return l;
}

/*
This function takes a vector l and returns a vector that contains the
elements that appear even number of times (or more) in l.
>>> count_even({1, 2, 3})
{3}
*/
#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> count_even(vector<float> l){
	int size = l.size();
	if (size % 2 != 1) return vector<int>();
	vector<int> res(0);
	for (int i=0;i<size;++i){
		if (l[i]%2 == 0) ++res[0];
	}
	return res;
}

// This problem is a little tricky, but I'm sure there are lots of solutions in the web.
/*
The function takes two vectors l and k and returns an index i such that l[i] == k for some i \in [1..size].

>>> match_val({0, 5}, {2, 9})
1
*/
#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using