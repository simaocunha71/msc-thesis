#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
vector<float> get_positive(vector<float> l){
    vector<float> positive;
    for(int i = 0; i < l.size(); i++){
        if(l[i] > 0){
            positive.push_back(l[i]);
        }
    }
    return positive;
}

B:
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
vector<float> get_positive(vector<float> l){
    vector<float> positive;
    for(int i = 0; i < l.size(); i++){
        if(l[i] >= 0){
            positive.push_back(l[i]);
        }
    }
    return positive;
}

C:
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
vector<float> get_positive(vector<float> l){
    vector<float> positive;
    for(int i = 0; i < l.size(); i++){
        if(l[i] < 0){
            continue;
        }
        positive.push_back(l[i]);
    }
    return positive;
}

D:
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
vector<float> get_positive(vector<float> l){
    vector<float> positive;
    for(int i = 0; i < l.size(); i++){
        if(l[i] > 0){
            positive.push_back(l[i]);
        }
        else if(l[i] < 0){
            continue;
        }
        else{
            positive.push_back(l[i]);
        }
    }
    return positive;
}

E:
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
vector<float> get_positive(vector<float> l){
    vector<float> positive;
    for(int i = 0; i < l.size(); i++){
        if(l[i] <= 0){
            continue;
        }
        positive.push_back(l[i]);
    }
    return positive;
}

F:
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
vector<float> get_positive(vector<float> l){
    vector<float> positive;
    for(int i = 0; i < l.size(); i++){
        if(l[i] >= 0){
            positive.push_back(l[i]);
        }
        else{
            continue;
        }
    }
    return positive;
}

G:
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
vector<float> get_positive(vector<float> l){
   