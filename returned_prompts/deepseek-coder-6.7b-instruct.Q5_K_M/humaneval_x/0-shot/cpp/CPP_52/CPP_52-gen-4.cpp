    for(int i = 0; i < l.size(); i++){
        if(l[i] >= t){
            return false;
        }
    }
    return true;
}
int main(){
    vector<int> l = {1, 2, 4, 10};
    int t = 100;
    printf(below_threshold(l, t) ? "true" : "false");
}

// Answer:
true
*/



