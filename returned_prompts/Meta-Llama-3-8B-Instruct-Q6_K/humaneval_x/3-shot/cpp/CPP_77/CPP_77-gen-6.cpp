    int root = round(pow(a, 1.0/3.0));
    return (root*root*root == a);
}
// or
bool iscuber(int a){
    for(int i = 0; i * i * i <= a; i++){
        if(i * i * i == a)
            return true;
    }
    return false;
}