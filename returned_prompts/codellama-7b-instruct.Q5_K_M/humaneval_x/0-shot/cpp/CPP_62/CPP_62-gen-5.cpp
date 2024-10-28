    int len = xs.size()-1;
    vector<float> ret(len);
    for(int i = 0; i < len; i++){
        ret[i] = xs[i+1];
    }
    return ret;
}

int main(){
    vector<float> xs;
    xs.push_back(1);
    xs.push_back(2);
    xs.push_back(3);
    vector<float> ret = derivative(xs);
    for(int i = 0; i < ret.size(); i++){
        printf("%f ", ret[i]);
    }
    return 0;
}
