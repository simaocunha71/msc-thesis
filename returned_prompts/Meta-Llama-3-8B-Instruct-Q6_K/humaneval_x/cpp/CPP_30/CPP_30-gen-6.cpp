    vector<float> v;
    for(int i = 0; i < l.size(); i++){
        if(l[i] > 0.0f){
            v.push_back(l[i]);
        }
    }
    return v;
}

int main(){
    vector<float> l = {-1, 2, -4, 5, 6};
    vector<float> result = get_positive(l);
    for(int i = 0; i < result.size(); i++){
        printf("%f ", result[i]);
    }
    return 0;
}

