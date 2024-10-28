    float max=l[0];
    for(int i=1;i<l.size();i++){
        if(l[i]>max){
            max=l[i];
        }
    }
    return max;

}
int main(){
    vector<float> l;
    l.push_back(1);
    l.push_back(2);
    l.push_back(3);
    float a=max_element(l);
    printf("%f\n",a);
    l.clear();
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
    a=max_element(l);
    printf("%f\n",a);
    return 0;
}



















































































































































































































































