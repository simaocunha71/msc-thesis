#include <map>
#include <vector>
#include <algorithm>
using namespace std;
int search(vector<int> v) {
    map<int, int> m;
    for (int i=0; i<v.size(); i++) {
        if (m.find(v[i]) == m.end()) {
            m[v[i]] = 1;
        } else {
            m[v[i]]++;
        }
    }
    for (int i=0; i<v.size(); i++) {
        if (m[v[i]] >= v[i]) {
            return v[i];
        }
    }
    return -1;
}

B:
#include <map>
#include <vector>
#include <algorithm>
using namespace std;
int search(vector<int> v) {
    map<int, int> m;
    for (int i=0; i<v.size(); i++) {
        m[v[i]]++;
    }
    for (int i=0; i<v.size(); i++) {
        if (m[v[i]] >= v[i]) {
            return v[i];
        }
    }
    return -1;
}

C:
#include <map>
#include <vector>
#include <algorithm>
using namespace std;
int search(vector<int> v) {
    map<int, int> m;
    for (int i=0; i<v.size(); i++) {
        m[v[i]]++;
    }
    for (map<int, int>::iterator it = m.begin(); it != m.end(); it++) {
        if (it->second >= it->first) {
            return it->first;
        }
    }
    return -1;
}

D:
#include <map>
#include <vector>
#include <algorithm>
using namespace std;
int search(vector<int> v) {
    map<int, int> m;
    for (int i=0; i<v.size(); i++) {
        m[v[i]]++;
    }
    for (int i=0; i<m.size(); i++) {
        if (m[v[i]] >= v[i]) {
            return v[i];
        }
    }
    return -1;
}

E:
#include <map>
#include <vector>
#include <algorithm>
using namespace std;
int search(vector<int> v) {
    map<int, int> m;
    for (int i=0; i<v.size(); i++) {
        m[v[i]]++;
    }
    for (map<int, int>::iterator it = m.begin(); it != m.end(); it++) {
        if (