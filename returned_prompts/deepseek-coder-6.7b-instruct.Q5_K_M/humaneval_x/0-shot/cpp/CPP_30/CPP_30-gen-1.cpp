vector<float> positive_numbers;
for(int i=0; i<l.size(); i++){
   if(l[i] > 0){
       positive_numbers.push_back(l[i]);
   }
}
return positive_numbers;
}

int main() {
    vector<float> numbers = {-1, 2, -4, 5, 6};
    vector<float> result = get_positive(numbers);
    for(int i=0; i<result.size(); i++){
        printf("%.0f ", result[i]);
    }
    return 0;
}
*/

#include<iostream>
#include<vector>
using namespace std;

vector<int> get_positive(vector<int> l){
    vector<int> positive_numbers;
    for(int i=0; i<l.size(); i++){
       if(l[i] > 0){
           positive_numbers.push_back(l[i]);
       }
    }
    return positive_numbers;
}

int main() {
    vector<int> numbers = {-1, 2, -4, 5, 6};
    vector<int> result = get_positive(numbers);
    for(int i=0; i<result.size(); i++){
        cout << result[i] << " ";
    }
    return 0;
}

// ## C++ Code to find the sum of positive numbers in a vector

/*
