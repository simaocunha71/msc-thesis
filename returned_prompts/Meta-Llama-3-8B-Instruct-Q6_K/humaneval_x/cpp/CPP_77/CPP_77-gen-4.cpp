    double root = cbrt(a);
    return round(root) == root;
}
int main(){
    printf("%d\n",iscuber(1)); //1
    printf("%d\n",iscuber(2)); //0
    printf("%d\n",iscuber(-1)); //1
    printf("%d\n",iscuber(64)); //1
    printf("%d\n",iscube(0)); //1
    printf("%d\n",iscube(180)); //0
    return 0;
}
