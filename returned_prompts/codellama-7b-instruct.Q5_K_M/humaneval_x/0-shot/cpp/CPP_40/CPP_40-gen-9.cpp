    for(int i = 0; i < l.size(); i++){
        if(l[i] == 0)
            return true;
    }
    for(int i = 0; i < l.size(); i++){
        for(int j = i + 1; j < l.size(); j++){
            if(l[i] + l[j] == 0)
                return true;
        }
    }
    return false;
}
int main(){
    vector<int> v = {2, 4, -5, 3, 9, 7};
    printf("%d\n", triples_sum_to_zero(v));
    return 0;
}
