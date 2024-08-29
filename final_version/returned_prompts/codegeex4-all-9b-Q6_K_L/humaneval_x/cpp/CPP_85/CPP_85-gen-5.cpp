#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;
int add(vector<int> lst){
    int sum=0;
    for(int i=1;i<lst.size();i+=2){
        if(lst[i]%2==0){
            sum+=lst[i];
        }
    }
    return sum;
}

C:
#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;
int add(vector<int> lst){
    int sum=0;
    for(int i=0;i<lst.size();i++){
        if(lst[i]%2==0&&i%2==1){
            sum+=lst[i];
        }
    }
    return sum;
}

D:
#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;
int add(vector<int> lst){
    int sum=0;
    for(int i=0;i<lst.size();i++){
        if(lst[i]%2==0&&i%2==0){
            sum+=lst[i];
        }
    }
    return sum;
}

E:
#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;
int add(vector<int> lst){
    int sum=0;
    for(int i=0;i<lst.size();i++){
        if(lst[i]%2==1&&i%2==0){
            sum+=lst[i];
        }
    }
    return sum;
}

F:
#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;
int add(vector<int> lst){
    int sum=0;
    for(int i=0;i<lst.size();i++){
        if(lst[i]%2==0&&i%2==1){
            sum+=lst[i];
        }
    }
    return sum;
}

