#include <vector>
using namespace std;

vector<int> pluck(vector<int> arr){
    if (arr.empty()) return {};
    int smallest = arr[0];
    int idx = 0;
    for (int i = 1; i < arr.size(); i++){
        if (arr[i] < smallest && arr[i] % 2 == 0){
            smallest = arr[i];
            idx = i;
        }
    }
    return {smallest, idx};
}

B:
#include <vector>
using namespace std;

vector<int> pluck(vector<int> arr){
    if (arr.empty()) return {};
    int smallest = arr[0];
    int idx = 0;
    for (int i = 1; i < arr.size(); i++){
        if (arr[i] < smallest && arr[i] % 2 == 0){
            smallest = arr[i];
            idx = i;
        }
    }
    return {smallest, idx};
}

C:
#include <vector>
using namespace std;

vector<int> pluck(vector<int> arr){
    if (arr.empty()) return {};
    int smallest = arr[0];
    int idx = 0;
    for (int i = 1; i < arr.size(); i++){
        if (arr[i] < smallest && arr[i] % 2 == 0){
            smallest = arr[i];
            idx = i;
        }
    }
    return {smallest, idx};
}

D:
#include <vector>
using namespace std;

vector<int> pluck(vector<int> arr){
    if (arr.empty()) return {};
    int smallest = arr[0];
    int idx = 0;
    for (int i = 1; i < arr.size(); i++){
        if (arr[i] < smallest && arr[i] % 2 == 0){
            smallest = arr[i];
            idx = i;
        }
    }
    return {smallest, idx};
}

E:
#include <vector>
using namespace std;

vector<int> pluck(vector<int> arr){
    if (arr.empty()) return {};
    int smallest = arr[0];
    int idx = 0;
    for (int i = 1; i < arr.size(); i++){
        if (arr[i] < smallest && arr[i] % 2 == 0){
            smallest = arr[i];
            idx = i;
        }
    }
    return {smallest, idx};
}

F:
#include <