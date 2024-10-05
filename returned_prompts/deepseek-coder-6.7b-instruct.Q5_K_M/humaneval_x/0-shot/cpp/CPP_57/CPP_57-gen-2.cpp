    for(int i=0; i<l.size()-1; i++){
        if(l[i+1]>l[i]){
            for(int j=i+1; j<l.size()-1; j++){
                if(l[j+1]<l[j]){
                    return false;
                }
            }
            return true;
        }
        else if(l[i+1]<l[i]){
            for(int j=i+1; j<l.size()-1; j++){
                if(l[j+1]>l[j]){
                    return false;
                }
            }
            return true;
        }
    }
    return true;
}
int main(){
    vector<float> vec1 {1, 2, 4, 20};
    vector<float> vec2 {1, 20, 4, 10};
    vector<float> vec3 {4, 1, 0, -10};
    printf("%d\n", monotonic(vec1)); //true
    printf("%d\n", monotonic(vec2)); //false
    printf("%d\n", monotonic(vec3)); //true
    return 0;
}
*/

