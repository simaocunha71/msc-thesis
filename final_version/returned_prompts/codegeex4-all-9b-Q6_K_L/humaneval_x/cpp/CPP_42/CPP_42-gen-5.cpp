    for (int i=0; i<l.size(); i++){
        l[i] += 1;
    }
    return l;
}
int main(){
    vector<int> v = {1, 2, 3};
    vector<int> ans = incr_list(v);
    for (int i=0; i<ans.size(); i++){
        printf("%d ", ans[i]);
    }
    printf("\n");
    return 0;
}

B:
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> incr_list(vector<int> l){
    for (int i=0; i<l.size(); i++){
        l[i] += 1;
    }
    return l;
}
int main(){
    vector<int> v = {1, 2, 3};
    vector<int> ans = incr_list(v);
    for (int i=0; i<ans.size(); i++){
        printf("%d ", ans[i]);
    }
    printf("\n");
    return 0;
}

C:
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> incr_vector(vector<int> v){
    for (int i=0; i<v.size(); i++){
        v[i] += 1;
    }
    return v;
}
int main(){
    vector<int> v = {1, 2, 3};
    vector<int> ans = incr_vector(v);
    for (int i=0; i<ans.size(); i++){
        printf("%d ", ans[i]);
    }
    printf("\n");
    return 0;
}

D:
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> incr_list(vector<int> v){
    for (int i=0; i<v.size(); i++){
        v[i] += 1;
    }
    return v;
}
int main(){
    vector<int> v = {1, 2, 3};
    vector<int> ans = incr_list(v);
    for (int i=0; i<ans.size(); i++){
        printf("%d ", ans[i]);
    }
    printf("\n");
    return 0;
}

The correct answer is C:

```C
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> incr_vector(vector<int> v){
    for (int i=0; i<v.size(); i++){
        v[i] += 1;
    }
    return v;
}
int main(){
    vector<int> v = {