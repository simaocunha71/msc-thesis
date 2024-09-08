#include <bits/stdc++.h>
#include <vector>
using namespace std;
bool will_it_fly(vector<int> q,int w){
    if (q.size() == 1) return q[0] <= w;
    for (int i = 0; i < q.size() / 2; i++) {
        if (q[i] != q[q.size() - 1 - i]) return false;
    }
    return accumulate(q.begin(), q.end(), 0) <= w;
}

B:
#include <bits/stdc++.h>
using namespace std;
bool will_it_fly(vector<int> q,int w){
    int sum = 0;
    for (int i=0;i<q.size();i++)
    {
        sum+=q[i];
    }
    for (int i=0;i<q.size()/2;i++)
    {
        if (q[i]!=q[q.size()-1-i]) return false;
    }
    return sum <= w;
}

C:
#include <bits/stdc++.h>
using namespace std;
bool will_it_fly(vector<int> q,int w){
    int sum = 0;
    for (int i = 0; i < q.size(); i++)
    {
        sum += q[i];
    }
    for (int i = 0; i < q.size() / 2; i++)
    {
        if (q[i] != q[q.size() - 1 - i]) return false;
    }
    return sum <= w;
}

D:
#include <bits/stdc++.h>
using namespace std;
bool will_it_fly(vector<int> q, int w) {
    int sum = 0;
    for (int i = 0; i < q.size(); i++) {
        sum += q[i];
    }
    for (int i = 0; i < q.size() / 2; i++) {
        if (q[i] != q[q.size() - 1 - i]) return false;
    }
    return sum <= w;
}
请问哪个代码片段是正确的？

选项A是正确的。

```cpp
#include <bits/stdc++.h>
#include <vector>
using namespace std;
bool will_it_fly(vector<int> q,int w){
    if (q.size() == 1) return q[0] <= w;
    for (int i = 0; i < q.size() / 2; i++) {
        if (q[i] != q[q