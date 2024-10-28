    for(int i=0; i<l.size(); i++){
        for(int j=i+1; j<l.size(); j++){
            for(int k=j+1; k<l.size(); k++){
                if(l[i]+l[j]+l[k]==0){
                    return true;
                }
            }
        }
    }
    return false;
}

int main(int argc, char** argv){
    vector<int> l = {1, 3, 5, 0};
    printf("%d\n", triples_sum_to_zero(l));
    vector<int> l2 = {1, 3, -2, 1};
    printf("%d\n", triples_sum_to_zero(l2));
    vector<int> l3 = {1, 2, 3, 7};
    printf("%d\n", triples_sum_to_zero(l3));
    vector<int> l4 = {2, 4, -5, 3, 9, 7};
    printf("%d\n", triples_sum_to_zero(l4));
    vector<int> l5 = {1};
    printf("%d\n", triples_sum_to_zero(l5));
    return 0;
}

