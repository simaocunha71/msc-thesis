    if(typeid(a) == typeid(b)){
        if(typeid(a) == typeid(double)){
            if(a<b)
                return b;
            else
                return a;
        }
        else if(typeid(a) == typeid(int)){
            if(a<b)
                return b;
            else
                return a;
        }
        else{
            if(a<b)
                return b;
            else
                return a;
        }
    }
    else if(typeid(a) == typeid(double)){
        if(a<b)
            return b;
        else
            return a;
    }
    else if(typeid(a) == typeid(int)){
        if(a<b)
            return b;
        else
            return a;
    }
    else{
        if(a<b)
            return b;
        else
            return a;
    }

}

int main(){
    double a = 2.5;
    int b = 1;
    boost::any c = 1, d = 2.5;
    printf("%f\n",compare_one(c,d));
    return 0;
}














































































































































































































