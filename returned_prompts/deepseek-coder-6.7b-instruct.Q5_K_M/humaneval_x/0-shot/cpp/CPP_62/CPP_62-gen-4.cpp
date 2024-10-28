    vector<float> res;
    int size = xs.size();
    for(int i=1; i<size; i++){
        res.push_back(i * xs[i]);
    }
    return res;
}

int main(){
    vector<float> coeff{3, 1, 2, 4, 5};
    vector<float> res = derivative(coeff);
    for(auto val: res){
        printf("%f ", val);
    }
    return 0;
}
```

### Python

```python
