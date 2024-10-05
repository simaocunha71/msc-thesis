    if(typeid(a)==typeid(b)){
        if(typeid(a)==typeid(string)){
            string sa=a.template get<string>();
            string sb=b.template get<string>();
            if(sa.find('.')!=string::npos&&sa.find('.')!=string::npos){
                sa=sa.substr(0,sa.find('.'));
                sb=sb.substr(0,sb.find('.'));
            }
            if(sa==sb){
                return "None";
            }
            if(sa>sb){
                return a;
            }
            return b;
        }
        if(a.template get<string>()==b.template get<string>()){
            return "None";
        }
        if(a.template get<string>()>b.template get<string>()){
            return a;
        }
        return b;
    }
    if(typeid(a)!=typeid(b)){
        if(a>b){
            return a;
        }
        return b;
    }
    return "None";
}

int main(){
    boost::any a,b;
    cin>>a>>b;
    cout<<compare_one(a,b)<<endl;
    return 0;
}

































































































































































































