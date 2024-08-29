#include <vector>
using namespace std;
vector<int> eat(int number, int need, int remaining) {
    int newNumber = number + need;
    int newRemaining = remaining - need;
    if (newRemaining < 0) {
        newRemaining = 0;
    }
    return {newNumber, newRemaining};
}

B:
#include <vector>
using namespace std;

vector<int> eat(int number, int need, int remaining){
    int newRemaining = remaining - need;
    if(newRemaining < 0){
        return {number+need,0};
    }else{
        return {number+need,newRemaining};
    }
}

C:
#include <vector>
using namespace std;

vector<int> eat(int number, int need, int remaining) {
    if (remaining < need) {
        return {number + remaining, 0};
    }
    return {number + need, remaining - need};
}

D:
#include <vector>
using namespace std;

vector<int> eat(int number, int need, int remaining) {
    int total = number + need;
    if (total <= remaining) {
        return {total, remaining - total};
    }
    return {remaining, 0};
}

E:
#include <vector>
using namespace std;
vector<int> eat(int number, int need, int remaining) {
    int newNumber = number + need;
    int newRemaining = remaining - need;
    if (newRemaining < 0) {
        newRemaining = 0;
    }
    return {newNumber, newRemaining};
}

F:
#include <vector>
using namespace std;

vector<int> eat(int number, int need, int remaining){
    if(need > remaining){
        number += remaining;
        remaining = 0;
    }else{
        number += need;
        remaining -= need;
    }
    return {number, remaining};
}

G:
#include <vector>
using namespace std;

vector<int> eat(int number, int need, int remaining) {
    int newNumber = number + need;
    int newRemaining = remaining - need;
    if (newRemaining < 0) {
        newRemaining = 0;
    }
    return {newNumber, newRemaining};
}

H:
#include <vector>
using namespace std;

vector<int> eat(int number, int need, int remaining) {
    int total = number + need;
    int newRemaining = remaining - need;
    if (newRemaining < 0) {
        newRemaining =