    for(int i = 0; i < l.size(); i++)
        for(int j = i + 1; j < l.size(); j++)
            if(l[i] + l[j] == 0)
                return true;
    return false;
}
// Tests
#include<vector>
#include<iostream>
int main(){
    vector<int> l1 = {1, 3, 5, 0};
    vector<int> l2 = {1, 3, -2, 1};
    vector<int> l3 = {1, 2, 3, 7};
    vector<int> l4 = {2, 4, -5, 3, 5, 7};
    vector<int> l5 = {1};

    cout << "pairs_sum_to_zero({1, 3, 5, 0}) = " << pairs_sum_to_zero(l1) << endl;
    cout << "pairs_sum_to_zero({1, 3, -2, 1}) = " << pairs_sum_to_zero(l2) << endl;
    cout << "pairs_sum_to_zero({1, 2, 3, 7}) = " << pairs_sum_to_zero(l3) << endl;
    cout << "pairs_sum_to_zero({2, 4, -5, 3, 5, 7}) = " << pairs_sum_to_zero(l4) << endl;
    cout << "pairs_sum_to_zero({1}) = " << pairs_sum_to_zero(l5) << endl;

    return 0;
}










































































































