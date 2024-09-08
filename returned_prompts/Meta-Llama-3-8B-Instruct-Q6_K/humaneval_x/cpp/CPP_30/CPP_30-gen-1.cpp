vector<float> result;
for(int i=0; i<l.size(); i++){
    if(l[i]>0)
        result.push_back(l[i]);
}
return result;
}

B:
vector<float> get_positive(vector<float> l){
    vector<float> result;
    for (float i : l) {
        if(i > 0) {
            result.push_back(i);
        }
    }
    return result;
}

C:
vector<float> get_positive(vector<float> l){
    vector<float> result = {i for i in l if i > 0};
    return result;
}

D:
vector<float> get_positive(vector<float> l){
    vector<float> result;
    for (int i = 0; i < l.size(); i++) {
        if (l[i] > 0) {
            result.push_back(l[i]);
        }
    }
    return result;
}

E:
vector<float> get_positive(vector<float> l){
    return vector<float>(std::remove_if(l.begin(), l.end(), [](float x){return x<0;}), l.end());
}

F:
vector<float> get_positive(vector<float> l){
    vector<float> result;
    for (float i : l) {
        if (i > 0) {
            result.push_back(i);
        }
    }
    return result;
}

G:
vector<float> get_positive(vector<float> l){
    vector<float> result;
    for (int i = 0; i < l.size(); i++) {
        if (l[i] > 0) {
            result.push_back(l[i]);
        }
    }
    return result;
}

H:
vector<float> get_positive(vector<float> l){
    vector<float> result;
    for (float i : l) {
        if(i > 0) {
            result.push_back(i);
        }
    }
    return result;
}

I:
vector<float> get_positive(vector<float> l){
    vector<float> result;
    for (int i = 0; i < l.size(); i++) {
        if(l[i] > 0) {
            result.push_back(l[i]);
        }
    }
    return result;
}

J:
vector<float> get_positive(vector<float> l){
    vector<float> result;
    for (float i : l) {
        if(i > 0) {
            result.push_back(i);
        }
    }
    return result;
}

K:
vector<float> get_positive(vector<float> l){
    vector