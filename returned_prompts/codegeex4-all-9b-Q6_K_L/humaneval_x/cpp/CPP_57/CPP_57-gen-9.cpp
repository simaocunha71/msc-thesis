#include <algorithm>
#include <vector>
using namespace std;
bool monotonic(vector<int> l){
    return is_sorted(l.begin(), l.end()) || is_sorted(l.rbegin(), l.rend());
}

B:
#include <algorithm>
#include <vector>
using namespace std;
bool monotonic(vector<int> l){
    return is_sorted(l.begin(), l.end()) || is_sorted(l.begin(), l.end(), greater<int>());
}

C:
#include <algorithm>
#include <vector>
using namespace std;
bool monotonic(vector<int> l){
    return is_sorted(l.begin(), l.end(), greater<int>()) || is_sorted(l.rbegin(), l.rend(), greater<int>());
}

D:
#include <algorithm>
#include <vector>
using namespace std;
bool monotonic(vector<int> l){
    return is_sorted(l.begin(), l.end()) || is_sorted(l.begin(), l.end(), less<int>());
}

E:
#include <algorithm>
#include <vector>
using namespace std;
bool monotonic(vector<int> l){
    return is_sorted(l.rbegin(), l.rend(), greater<int>()) || is_sorted(l.begin(), l.end(), less<int>());
}

F:
#include <algorithm>
#include <vector>
using namespace std;
bool monotonic(vector<int> l){
    return is_sorted(l.begin(), l.end(), less<int>()) || is_sorted(l.rbegin(), l.rend(), greater<int>());
}

G:
#include <algorithm>
#include <vector>
using namespace std;
bool monotonic(vector<int> l){
    return is_sorted(l.begin(), l.end(), greater<int>()) || is_sorted(l.rbegin(), l.rend());
}

H:
#include <algorithm>
#include <vector>
using namespace std;
bool monotonic(vector<int> l){
    return is_sorted(l.begin(), l.end(), greater<int>()) || is_sorted(l.end(), l.rbegin(), less<int>());
}

I:
#include <algorithm>
#include <vector>
using namespace std;
bool monotonic(vector<int> l){
    return is_sorted(l.begin(), l.end()) || is_sorted(l.end(), l.rbegin(), greater<int>());
}

J:
#include <algorithm>
#include <vector>
using namespace std;
bool monotonic(vector<int> l){
    return is_sorted(l.end(), l.rbegin(), greater<int>()) || is_sorted(l.begin(), l.end(), less<int>());
}

K:
#include <algorithm>
#include <vector>
using namespace std;
bool monotonic(vector<int> l){
    return is_sorted(l.begin(), l.end(), greater<int>()) || is_sorted(l