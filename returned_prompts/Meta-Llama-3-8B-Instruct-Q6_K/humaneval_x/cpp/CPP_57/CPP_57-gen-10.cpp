    if(l.size()==1) return true;
    bool increasing = true;
    bool decreasing = true;
    for(int i = 1; i < l.size(); i++){
        if(l[i] > l[i-1]){
            decreasing = false;
        }
        else if(l[i] < l[i-1]){
            increasing = false;
        }
    }
    return increasing || decreasing;
}
int main() {
    vector<float> l = {1,2,4,20};
    cout << monotonic(l) << endl;
    return 0;
}
