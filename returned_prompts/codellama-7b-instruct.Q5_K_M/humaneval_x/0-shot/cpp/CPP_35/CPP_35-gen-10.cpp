    float a = 0;
    for (int i = 0; i < l.size(); i++){
        if (l[i] > a){
            a = l[i];
        }
    }
    return a;
}
int main(){
    vector<float> l;
    l.push_back(1);
    l.push_back(2);
    l.push_back(3);
    float b = max_element(l);
    printf("%f\n", b);
}

