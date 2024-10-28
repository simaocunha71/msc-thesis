    for (int i = 0; i < l.size()-1; i++){
        if (l[i] < l[i+1]){
            continue;
        }
        else if (l[i] > l[i+1]){
            for (int j = i+1; j < l.size()-1; j++){
                if (l[j] > l[j+1]){
                    continue;
                }
                else{
                    return false;
                }
            }
            return true;
        }
        else{
            continue;
        }
    }
    return true;
}


int main(){
    vector<float> v1 = {1, 2, 4, 20};
    vector<float> v2 = {1, 20, 4, 10};
    vector<float> v3 = {4, 1, 0, -10};
    printf("%d\n", monotonic(v1));
   