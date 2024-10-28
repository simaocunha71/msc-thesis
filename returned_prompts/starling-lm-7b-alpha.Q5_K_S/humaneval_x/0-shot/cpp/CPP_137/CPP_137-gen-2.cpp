    if(typeid(a)==typeid(b)){
        if(typeid(a)==typeid(int)){
            if((int)a>(int)b)return a;
            else if((int)a==(int)b)return "None";
            else return b;
        }else if(typeid(a)==typeid(float)){
            if((float)a>(float)b)return a;
            else if((float)a==(float)b)return "None";
            else return b;
        }else if(typeid(a)==typeid(double)){
            if((double)a>(double)b)return a;
            else if((double)a==(double)b)return "None";
            else return b;
        }else if(typeid(a)==typeid(string)){
            if(((string)a).size()<((string)b).size())return a;
            else if(((string)a).size()==((string)b).size())return "None";
            else return b;
        }
    }else if(typeid(a)==typeid(int)||typeid(a)==typeid(float)||typeid(a)==typeid(double)){
        if((int)a>(float)b)return a;
        else if((int)a==(float)b)return "None";
        else return b;
    }else if(typeid(a)==typeid(int)||typeid(a)==typeid(double)){
        if((int)a>(double)b)return a;
        else if((int)a==(double)b)return "None";
        else return b;
    }else if(typeid(a)==typeid(int)||typeid(a)==typeid(string)){
        if((int)a>(string)b)return a;
        else if((int)a==(string)b)return "None";
        else return b;
    }
    goto A;
}


int main()
{
    return 0;
}



















