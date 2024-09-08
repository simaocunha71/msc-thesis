    sort(l.begin(), l.end());
    int size = l.size();
    if(size % 2 == 1){
        return l[size/2];
    }else{
        return (l[size/2 - 1] + l[size/2]) / 2.0;
    }
}

int main(){
    vector<float> l = {3, 1, 2, 4, 5};
    printf("%f\n", median(l));
    l = {4, 6, 1000, 10, 20, -10};
    printf("%f\n", median(l));
    return 0;
}

