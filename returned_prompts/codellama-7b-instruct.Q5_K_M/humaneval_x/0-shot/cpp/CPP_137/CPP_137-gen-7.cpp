
    if(a.type()!=b.type()){
        goto A;
    }
    if(a==b){
        return "None";
    }
    if(a.type()==typeid(int)){
        return (int)a > (int)b ? a : b;
    }
    if(a.type()==typeid(float)){
        return (float)a > (float)b ? a : b;
    }
    if(a.type()==typeid(string)){
        return a.get_value<string>() > b.get_value<string>() ? a : b;
    }
}


