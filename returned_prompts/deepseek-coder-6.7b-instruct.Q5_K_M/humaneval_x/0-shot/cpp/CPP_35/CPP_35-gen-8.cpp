    float max_val = l[0];
    for (int i=0; i<l.size(); i++){
        if (l[i]>max_val){
            max_val = l[i];
        }
    }
    return max_val;
}
int main() {
    vector<float> l;
    l.push_back(5);
    l.push_back(3);
    l.push_back(-5);
    l.push_back(2);
    l.push_back(-3);
    l.push_back(3);
    l.push_back(9);
    l.push_back(0);
    l.push_back(123);
    l.push_back(1);
    l.push_back(-10);
    printf("%f\n", max_element(l));
    return 0;
}

