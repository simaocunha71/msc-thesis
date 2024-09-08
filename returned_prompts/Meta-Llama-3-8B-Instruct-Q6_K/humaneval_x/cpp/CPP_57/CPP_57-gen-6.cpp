    for(int i=1;i<l.size();i++){
        if(l[i-1]>l[i]&&l[i-1]-l[i]>0.00001)
            return false;
        if(l[i-1]<l[i]&&l[i-1]-l[i]<0.00001)
            return false;
    }
    return true;
}

int main() {
    vector<float> v = {1, 2, 4, 20};
    printf("%d\n", monotonic(v));
    return 0;
}

