    vector<float> result;
    result.push_back(0);
    for(int i = 1; i < xs.size(); i++){
        result.push_back(i*xs[i]);
    }
    return result;
}
int main() {
    vector<float> xs = {3, 1, 2, 4, 5};
    vector<float> result = derivative(xs);
    for(int i = 0; i < result.size(); i++){
        printf("%f ", result[i]);
    }
    return 0;
}

