    vector<int> y;
    for(int i=0; i<x.size(); i++){
        if(x[i]%2==1){
            y.push_back(x[i]);
        }
    }
    sort(y.begin(), y.end());
    return y;
}

int main(){
    vector<int> x = {15, 33, 1422, 1};
    vector<int> y = unique_digits(x);
    for(int i=0; i<y.size(); i++){
        printf("%d ", y[i]);
    }
    printf("\n");
}

