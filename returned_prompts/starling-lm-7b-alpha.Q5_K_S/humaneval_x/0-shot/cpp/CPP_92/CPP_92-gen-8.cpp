    
    if(fabs(a+b)==fabs(c)){
        return true;
    }
    else if(fabs(b+c)==fabs(a)){
        return true;
    }
    else if(fabs(c+a)==fabs(b)){
        return true;
    }
    else{
        return false;
    }
    goto A;
```