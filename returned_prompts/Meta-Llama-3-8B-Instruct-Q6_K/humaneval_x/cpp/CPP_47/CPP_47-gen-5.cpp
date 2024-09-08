    sort(l.begin(),l.end());
    float med;
    if(l.size()%2==0){
        med = (l[l.size()/2-1]+l[l.size()/2])/2.0;
    }
    else{
        med = l[l.size()/2];
    }
    return med;
}

int main(){
    vector<float> v = {3, 1, 2, 4, 5};
    printf("%f\n",median(v));
    return 0;
}
