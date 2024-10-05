
#include<iostream>
#include<vector>
using namespace std;
vector<double> derivative(vector<double> xs){
    vector<double> ret;
    ret.push_back(xs[1]);
    for(int i = 2; i < xs.size(); i++) {
        ret.push_back(ret[i-2] + xs[i]*i);
    }
    return ret;
}

int main(void){
    vector<double> xs = {3, 1, 2, 4, 5};
    vector<double> ret = derivative(xs);
    for(int i = 0; i < ret.size(); i++) {
        cout << ret[i] << " ";
    }
    cout << endl;
    xs = {1, 2, 3};
    ret = derivative(xs);
    for(int i = 0; i < ret.size(); i++) {
        cout << ret[i] << " ";
    }
    cout << endl;
}





































