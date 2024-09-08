    vector<float> res;
    if(xs.size() == 0) return res;
    res.push_back(xs[1]);
    for(int i = 1; i < xs.size() - 1; i++){
        res.push_back(res.back() + i * xs[i]);
    }
    return res;
}
int main(){
    vector<float> xs = {3, 1, 2, 4, 5};
    vector<float> res = derivative(xs);
    for(float i : res) printf("%f ", i);
    printf("\n");
    return 0;
}
