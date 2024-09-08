    vector<int> result;
    result.push_back(n);
    int prev = n;
    while (n > 1) {
        n = (n % 2 == 0) ? n - 1 : n + 1;
        result.push_back(n);
        prev = n;
    }
    result.push_back(1);
    return result;
}

int main() {
    int n;
    printf("Enter the number of levels:");
    scanf("%d", &n);
    vector<int> res = make_a_pile(n);
    printf("Number of stones in each level: ");
    for(int i=0; i<res.size(); i++){
        printf("%d ", res[i]);
    }
    printf("\n");
    return 0;
}
B:
    #include<bits/stdc++.h>
    using namespace std;
    vector<int> make_a_pile(int n){
        vector<int> result;
        result.push_back(n);
        int prev = n;
        while (n > 1) {
            n = (n % 2 == 0) ? n - 1 : n + 1;
            result.push_back(n);
            prev = n;
        }
        result.push_back(1);
        return result;
    }
    int main() {
        int n;
        cout << "Enter the number of levels: ";
        cin >> n;
        vector<int> res = make_a_pile(n);
        cout << "Number of stones in each level: ";
        for(int i=0; i<res.size(); i++){
            cout << res[i] << " ";
        }
        cout << "\n";
        return 0;
    }
C:
    #include <iostream>
    #include <vector>
    using namespace std;
    vector<int> make_a_pile(int n) {
        vector<int> result;
        result.push_back(n);
        int prev = n;
        while (n > 1) {
            n = (n % 2 == 0) ? n - 1 : n + 1;
            result.push_back(n);
            prev = n;
        }
        result.push_back(1);
        return result;
    }
    int main() {
        int n;
        cout << "Enter the number of levels: ";
        cin >> n;
        vector<int> res = make_a_pile(n);
        cout << "Number of stones in each level: ";
        for(int i=0; i<