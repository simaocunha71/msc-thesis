    float a_f,b_f;
    string a_s,b_s;
    if (boost::any_cast<float>(a)==boost::any_cast<float>(b)){
        return "None";
    }
    else if (boost::any_cast<string>(a)!="None"){
        a_s=boost::any_cast<string>(a);
        b_s=boost::any_cast<string>(b);
        if (a_s.find(".")==-1 && b_s.find(".")==-1){
            if (a_s<b_s) return b_s;
            else return a_s;
        }
        if (a_s.find(".")!=-1 && b_s.find(".")==-1){
            if (a_s<b_s) return b_s;
            else return a_s;
        }
        if (a_s.find(".")!=-1 && b_s.find(".")!=-1){
            a_f=boost::any_cast<float>(a);
            b_f=boost::any_cast<float>(b);
            if (a_f<b_f) return b_s;
            else return a_s;
        }
    }
    else if (boost::any_cast<float>(a)!=boost::any_cast<float>(b)){
        a_f=boost::any_cast<float>(a);
        b_f=boost::any_cast<float>(b);
        if (a_f<b_f) return b_f;
        else return a_f;
    }
}


