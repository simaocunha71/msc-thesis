#include <vector>
using namespace std;

int solution(vector<int> lst) {
    int sum = 0;
    for(int i=0; i<lst.size(); i+=2) {
        if(lst[i]%2==1) {
            sum+=lst[i];
        }
    }
    return sum;
}
B:
#include <vector>
using namespace std;

int solution(vector<int> lst) {
    int sum = 0;
    for(int i=0; i<lst.size(); i+=2) {
        if(lst[i]%2==1) {
            sum += lst[i];
        }
    }
    return sum;
}

C:
#include <vector>
using namespace std;

int solution(vector<int> lst) {
    int sum = 0;
    for(int i=0; i<lst.size(); i++) {
        if(i%2==1) {
            if(lst[i]%2==1) {
                sum += lst[i];
            }
        }
    }
    return sum;
}

D:
#include <vector>
using namespace std;

int solution(vector<int> lst) {
    int sum = 0;
    for(int i=0; i<lst.size(); i++) {
        if(i%2==1) {
            if(lst[i]%2==1) {
                sum+=lst[i];
            }
        }
    }
    return sum;
}

E:
#include <vector>
using namespace std;

int solution(vector<int> lst) {
    int sum = 0;
    for(int i=0; i<lst.size(); i++) {
        if(i%2==0) {
            if(lst[i]%2==1) {
                sum+=lst[i];
            }
        }
    }
    return sum;
}

F:
#include <vector>
using namespace std;

int solution(vector<int> lst) {
    int sum = 0;
    for(int i=0; i<lst.size(); i++) {
        if(i%2==1) {
            if(lst[i]%2==0) {
                sum+=lst[i];
            }
        }
    }
    return sum;
}

G:
#include <vector>
using namespace std;

int solution(vector<int> lst) {
    int sum = 0;
    for(int i=0; i<lst.size(); i++) {
        if(i%2==0) {
            if(lst[i]%2==0) {
                sum+=lst[i];
            }
        }
    }
    return sum;
}
