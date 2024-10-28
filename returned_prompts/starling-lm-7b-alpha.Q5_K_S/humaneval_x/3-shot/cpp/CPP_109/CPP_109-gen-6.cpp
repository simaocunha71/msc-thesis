    vector<int>::iterator i,max;
    int n=arr.size();
    if (n==0)
    return true;

    i=arr.begin();
    max=i;
    while(i!=arr.end()){
        if (*i>*(max)){
            max=i;
        }
        i++;
    }
    i=arr.begin();
    while(i!=arr.end()){
        if (*i<*(max)){
            i++;
        }else{
            arr.erase(i);
        }
    }

    if (max==arr.begin())
    return true;
    else
    return false;
}



