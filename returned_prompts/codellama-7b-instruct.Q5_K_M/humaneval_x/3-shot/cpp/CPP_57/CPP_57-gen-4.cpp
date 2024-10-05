    int i;
    int direction=0;
    float last=0;
    float current;
    for (i=0;i<l.size();i++){
        current=l[i];
        if (i==0)
        last=current;
        if (current>last)
        {
            if (direction==-1)
            return false;
            direction=1;
        }
        else if (current<last)
        {
            if (direction==1)
            return false;
            direction=-1;
        }
        last=current;
    }
    return true;
}



