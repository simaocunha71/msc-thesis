    vector<int> result;
    for(int i=0; i<x.size(); i++){
        int num = x[i];
        bool isUnique = true;
        while(num > 0){
            int digit = num % 10;
            if(digit % 2 == 0){
                isUnique = false;
                break;
            }
            num /= 10;
        }
        if(isUnique){
            result.push_back(x[i]);
        }
    }
    sort(result.begin(), result.end());
    return result;
}

int main() {
    vector<int> x = {15, 33, 1422, 1};
    vector<int> res = unique_digits(x);
    for(int i=0; i<res.size(); i++)
        printf("%d ", res[i]);
    return 0;
}

/*
Output:
1 15 33 
*/


A: 
    vector<int> result;
    for(int i=0; i<x.size(); i++){
        int num = x[i];
        bool isUnique = true;
        while(num > 0){
            int digit = num % 10;
            if(digit % 2 == 0){
                isUnique = false;
                break;
            }
            num /= 10;
        }
        if(isUnique){
            result.push_back(x[i]);
        }
    }
    sort(result.begin(), result.end());
    return result;
}

int main() {
    vector<int> x = {15, 33, 1422, 1};
    vector<int> res = unique_digits(x);
    for(int i=0; i<res.size(); i++)
        printf("%d ", res[i]);
    return 0;
}

/*
Output:
1 15 33 
*/

This program will iterate over the input vector and for each element, it