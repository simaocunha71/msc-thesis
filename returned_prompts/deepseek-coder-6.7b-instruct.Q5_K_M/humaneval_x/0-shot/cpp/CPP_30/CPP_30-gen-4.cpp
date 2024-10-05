    vector<float> result;
    for (float i : l)
        if (i > 0)
            result.push_back(i);
    return result;
}
int main(){
    vector<float> v = {-1, 2, -4, 5, 6};
    vector<float> res = get_positive(v);
    for(float i : res)
        printf("%.0f ", i);
    return 0;
}
```

