    if(a.type()==typeid(int)){
        if(b.type()==typeid(int)){
            if(a<b)return b;
            else return a;
        }
        else if(b.type()==typeid(float)){
            if(a<b)return b;
            else return a;
        }
        else if(b.type()==typeid(string)){
            if(a<stoi(b.get<string>()))return stoi(b.get<string>());
            else return a;
        }
    }
    else if(a.type()==typeid(float)){
        if(b.type()==typeid(int)){
            if(a<b)return b;
            else return a;
        }
        else if(b.type()==typeid(float)){
            if(a<b)return b;
            else return a;
        }
        else if(b.type()==typeid(string)){
            if(a<stod(b.get<string>()))return stod(b.get<string>());
            else return a;
        }
    }
    else if(a.type()==typeid(string)){
        if(b.type()==typeid(int)){
            if(stoi(a.get<string>())<b)return b;
            else return a;
        }
        else if(b.type()==typeid(float)){
            if(stod(a.get<string>())<b)return b;
            else return a;
        }
        else if(b.type()==typeid(string)){
            if(stoi(a.get<string>())<stoi(b.get<string>()))return b.get<string>();
            else return a.get<string>();
        }
    }
    return "None";

}

int main(){
    printf("%s\n",compare_one(1,2.5).type().name());
    printf("%s\n",compare_one(1,"2,3").type().name());
    printf("%s\n",compare_one("5,1