#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> largest_smallest_integers(vector<int> lst){
    int max = 0;
    int min = 0;
    for(int i = 0; i < lst.size(); i++){
        if(lst[i] > max && lst[i] < 0){
            max = lst[i];
        }
        if(lst[i] < min && lst[i] > 0){
            min = lst[i];
        }
    }
    vector<int> result{max,min};
    return result;
}

int main() {
    vector<int> a = {2, 4, 1, 3, 5, 7};
    vector<int> b = {0};
    vector<int> c = {-1,2,3,4,5,6};
    vector<int> d = {1,2,3,4,5,6};
    vector<int> e = {-1,2,3,-4,5,6};

    vector<int> x = largest_smallest_integers(a);
    vector<int> y = largest_smallest_integers(b);
    vector<int> z = largest_smallest_integers(c);
    vector<int> w = largest_smallest_integers(d);
    vector<int> v = largest_smallest_integers(e);

    for(int i : x){
        cout << i << " ";
    }
    cout << endl;
    for(int i : y){
        cout << i << " ";
    }
    cout << endl;
    for(int i : z){
        cout << i << " ";
    }
    cout << endl;
    for(int i : w){
        cout << i << " ";
    }
    cout << endl;
    for(int i : v){
        cout << i << " ";
    }

    return 0;
}