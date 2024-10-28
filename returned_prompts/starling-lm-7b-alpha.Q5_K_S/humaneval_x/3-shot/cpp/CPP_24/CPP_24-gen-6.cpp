    int i,div=n;
    for (i=2;i<n;i++)
    if (n%i==0){
        div=i;
        break;
    }
    return div;
}


