#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
bool is_sorted(vector<int> lst){
    for(int i = 0; i < lst.size(); i++){
        if(lst[i] != lst[i + 1]) return false;
    }
    return true;
}
B:
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
bool is_sorted(vector<int> lst){
    int count = 0;
    for(int i = 0; i < lst.size() - 1; i++){
        if(lst[i] > lst[i + 1]) return false;
    }
    for(int i = 0; i < lst.size() - 1; i++){
        if(lst[i] == lst[i + 1]) count++;
        if(count > 1) return false;
    }
    return true;
}
C:
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
bool is_sorted(vector<int> lst){
    int count = 0;
    for(int i = 0; i < lst.size() - 1; i++){
        if(lst[i] == lst[i + 1]) count++;
        if(count > 1) return false;
    }
    for(int i = 0; i < lst.size() - 1; i++){
        if(lst[i] > lst[i + 1]) return false;
    }
    return true;
}
D:
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
bool is_sorted(vector<int> lst){
    int count = 0;
    for(int i = 0; i < lst.size() - 1; i++){
        if(lst[i] > lst[i + 1]) return false;
    }
    return true;
}
E:
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
bool is_sorted(vector<int> lst){
    int count = 0;
    for(int i = 0; i < lst.size() - 1; i++){
        if(lst[i] == lst[i + 1]) count++;
        if(count > 1) return false;
    }
    return true;
}
F:
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
bool is_sorted(vector<int> lst){
    int count = 0;
    for(int i = 0; i < lst.size() - 1; i++){
        if(lst[i] == lst[i + 1]) count++;
    }
