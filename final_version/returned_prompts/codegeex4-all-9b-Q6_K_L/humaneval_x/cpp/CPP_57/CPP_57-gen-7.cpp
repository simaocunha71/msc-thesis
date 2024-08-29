bool increasing = true, decreasing = true;
for (int i = 0; i < l.size()-1; i++){
    if (l[i+1] < l[i]) decreasing = false;
    if (l[i+1] > l[i]) increasing = false;
}
return increasing || decreasing;
}
B:
bool monotonic(vector<float> l){
    bool increasing = true, decreasing = true;
    for (int i = 0; i < l.size()-1; i++){
        if (l[i+1] < l[i]) decreasing = false;
        if (l[i+1] > l[i]) increasing = false;
    }
    return increasing && decreasing;
}
C:
bool monotonic(vector<float> l){
    bool increasing = true, decreasing = true;
    for (int i = 0; i < l.size()-1; i++){
        if (l[i+1] < l[i]) decreasing = false;
        if (l[i+1] > l[i]) increasing = false;
    }
    return !increasing || !decreasing;
}
D:
bool monotonic(vector<float> l){
    bool increasing = true, decreasing = true;
    for (int i = 0; i < l.size()-1; i++){
        if (l[i+1] < l[i]) decreasing = false;
        if (l[i+1] > l[i]) increasing = false;
    }
    return !increasing && !decreasing;
}
E:
bool monotonic(vector<float> l){
    bool increasing = true, decreasing = true;
    for (int i = 0; i < l.size()-1; i++){
        if (l[i+1] < l[i]) decreasing = false;
        if (l[i+1] > l[i]) increasing = false;
    }
    return increasing || decreasing;
}
F:
bool monotonic(vector<float> l){
    bool increasing = true, decreasing = true;
    for (int i = 0; i < l.size()-1; i++){
        if (l[i+1] < l[i]) decreasing = false;
        if (l[i+1] > l[i]) increasing = false;
    }
    return increasing && decreasing;
}
G:
bool monotonic(vector<float> l){
    bool increasing = true, decreasing = true;
    for (int i = 0; i < l.size()-1; i++){
        if (l[i+