    vector<float> res;
    int n = xs.size();
    for(int i = 1; i < n; i++){
        res.push_back(xs[i] * i);
    }
    return res;
}
int main() {
    vector<float> xs = {3, 1, 2, 4, 5};
    vector<float> res = derivative(xs);
    for (float x: res) {
        printf("%f ", x);
    }
    printf("\n");
    return 0;
}
