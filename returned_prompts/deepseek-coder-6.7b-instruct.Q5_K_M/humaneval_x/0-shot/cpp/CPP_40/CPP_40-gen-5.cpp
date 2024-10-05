    for (int i=0; i<l.size(); i++){
        for (int j=i+1; j<l.size(); j++){
            for (int k=j+1; k<l.size(); k++){
                if (l[i]+l[j]+l[k] == 0){
                    return true;
                }
            }
        }
    }
    return false;
}

int main(){
    vector<int> test1 = {1, 3, 5, 0};
    vector<int> test2 = {1, 3, -2, 1};
    vector<int> test3 = {1, 2, 3, 7};
    vector<int> test4 = {2, 4, -5, 3, 9, 7};
    vector<int> test5 = {1};

    printf("%d\n", triples_sum_to_zero(test1)); //false
    printf("%d\n", triples_sum_to_zero(test2)); //true
    printf("%d\n", triples_sum_to_zero(test3)); //false
    printf("%d\n", triples_sum_to_zero(test4)); //true
    printf("%d\n", triples_sum_to_zero(test5)); //false

    return 0;
}

*/

