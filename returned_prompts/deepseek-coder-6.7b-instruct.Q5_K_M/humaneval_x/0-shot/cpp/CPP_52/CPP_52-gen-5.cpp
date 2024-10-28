    for (int i=0; i<l.size(); i++){
        if (l[i] >= t){
            return false;
        }
    }
    return true;
}
int main() {
    vector<int> v1 = {1, 2, 4, 10};
    vector<int> v2 = {1, 20, 4, 10};
    printf(below_threshold(v1, 100) ? "true" : "false");
    printf(below_threshold(v2, 5) ? "true" : "false");
    return 0;
}

*/

// C++
/*
