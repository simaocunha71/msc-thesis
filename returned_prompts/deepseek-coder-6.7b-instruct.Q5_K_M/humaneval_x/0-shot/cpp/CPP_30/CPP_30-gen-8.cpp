    vector<float> result;
    for(int i=0; i<l.size(); i++){
        if(l[i] > 0){
            result.push_back(l[i]);
        }
    }
    return result;
}

int main(){
    vector<float> l1 = {-1, 2, -4, 5, 6};
    vector<float> l2 = {5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10};
    vector<float> result1 = get_positive(l1);
    vector<float> result2 = get_positive(l2);
    for(int i=0; i<result1.size(); i++){
        printf("%.0f ",result1[i]);
    }
    printf("\n");
    for(int i=0; i<result2.size(); i++){
        printf("%.0f ",result2[i]);
    }
    return 0;
}
```

### C++ Program to Convert Decimal to Binary

