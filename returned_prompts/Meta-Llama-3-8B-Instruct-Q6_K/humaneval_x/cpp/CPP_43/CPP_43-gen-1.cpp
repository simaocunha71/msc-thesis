    for(int i=0;i<l.size();i++){
        for(int j=i+1;j<l.size();j++){
            if(l[i]+l[j]==0){
                return true;
            }
        }
    }
    return false;
}
int main(int argc, char const *argv[]) {
    vector<int> v1 = {1, 3, 5, 0};
    vector<int> v2 = {1, 3, -2, 1};
    vector<int> v3 = {1, 2, 3, 7};
    vector<int> v4 = {2, 4, -5, 3, 5, 7};
    vector<int> v5 = {1};

    cout << pairs_sum_to_zero(v1) << endl;
    cout << pairs_sum_to_zero(v2) << endl;
    cout << pairs_sum_to_zero(v3) << endl;
    cout << pairs_sum_to_zero(v4) << endl;
    cout << pairs_sum_to_zero(v5) << endl;

    return 0;
}

B:
    #include <iostream>
    #include <vector>
    #include <algorithm>
    using namespace std;

    bool pairs_sum_to_zero(vector<int> l) {
        set<int> s(l.begin(), l.end());
        for (int i : s) {
            if (s.count(-i)) {
                return true;
            }
        }
        return false;
    }

    int main() {
        vector<int> v1 = {1, 3, 5, 0};
        vector<int> v2 = {1, 3, -2, 1};
        vector<int> v3 = {1, 2, 3, 7};
        vector<int> v4 = {2, 4, -5, 3, 5, 7};
        vector<int> v5 = {1};

        cout << pairs_sum_to_zero(v1) << endl;
        cout << pairs_sum_to_zero(v2) << endl;
        cout << pairs_sum_to_zero(v3) << endl;
        cout << pairs_sum_to_zero(v4) << endl;
        cout << pairs_sum_to_zero(v5) << endl;

        return 0;
    }

C:
    #include <iostream>
    #include <vector>
    #include <algorithm>
    using namespace std;

    bool pairs_sum_to_zero(vector<int> l) {
        set