int main() {
    vector<float> xs = {3, 1, 2, 4, 5};
    auto res = derivative(xs);
    for (auto x : res) {
        printf("%f ", x);
    }
    return 0;
}


B:
#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

vector<float> derivative(vector<float> xs) {
    int size = xs.size();
    vector<float> res(size - 1);
    for (int i = 1; i < size; i++) {
        res[i - 1] = i * xs[i];
    }
    return res;
}

int main() {
    vector<float> xs = {3, 1, 2, 4, 5};
    vector<float> res = derivative(xs);
    for (int i = 0; i < res.size(); i++) {
        cout << res[i] << " ";
    }
    cout << endl;
    return 0;
}

C:
#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

vector<float> derivative(vector<float> xs) {
    int size = xs.size();
    vector<float> res(size - 1);
    for (int i = 1; i < size; i++) {
        res