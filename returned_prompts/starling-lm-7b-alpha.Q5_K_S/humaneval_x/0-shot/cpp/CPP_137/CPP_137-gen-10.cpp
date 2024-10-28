    if (typeid(a)==typeid(b)){
        if (typeid(a)==typeid(string)){
            string a1=boost::any_cast<string>(a);
            string b1=boost::any_cast<string>(b);
            if (a1==b1) return "None";
            if (a1.size()>b1.size()) return a1;
            else return b1;
        }
        return boost::any_cast<int>(a)>boost::any_cast<int>(b)?a:b;
    }else if (typeid(a)==typeid(int)){
        if (typeid(b)==typeid(string)) return b;
        if (typeid(b)==typeid(int)) return boost::any_cast<int>(a)>boost::any_cast<int>(b)?a:b;
    }else if (typeid(a)==typeid(float)){
        if (typeid(b)==typeid(string)) return b;
        if (typeid(b)==typeid(float)) return boost::any_cast<float>(a)>boost::any_cast<float>(b)?a:b;
    }else if (typeid(a)==typeid(double)){
        if (typeid(b)==typeid(string)) return b;
        if (typeid(b)==typeid(double)) return boost::any_cast<double>(a)>boost::any_cast<double>(b)?a:b;
    }else if (typeid(a)==typeid(long double)){
        if (typeid(b)==typeid(string)) return b;
        if (typeid(b)==typeid(long double)) return boost::any_cast<long double>(a)>boost::any_cast<long double>(b)?a:b;
    }
    return a;
}
int main(){
    boost::any a,b;
    a=1;b=2.5;printf("%d\n",compare_one(a,b).type());
    a=1;b="2,3";printf("%d\n",compare_one(a,b).