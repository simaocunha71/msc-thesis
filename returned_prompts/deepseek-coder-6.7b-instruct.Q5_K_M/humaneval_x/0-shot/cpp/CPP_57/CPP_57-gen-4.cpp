    for(int i = 0; i < l.size()-1; i++){
        if(l[i]>l[i+1])
            return false;
    }
    return true;
}
int main(){
    vector<float> l={1, 2, 4, 20};
    printf(monotonic(l) ? "true\n" : "false\n");
    return 0;
}

This code checks if the vector elements are in non-decreasing order. If the elements are in non-decreasing order, it returns true. If not, it returns false.



