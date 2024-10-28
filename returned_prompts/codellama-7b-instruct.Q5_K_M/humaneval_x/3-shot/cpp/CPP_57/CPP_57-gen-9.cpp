    int i;
    float diff=l[1]-l[0];
    for (i=1;i<l.size();i++){
        if (diff*l[i]-l[i-1]<0)
            return false;
    }
    return true;
}



