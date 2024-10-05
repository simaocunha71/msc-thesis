if(a.type()==typeid(string) && b.type()==typeid(string)){
    string a_str=boost::any_cast<string>(a);
    string b_str=boost::any_cast<string>(b);
    if(a_str==b_str) return "None";
    if(a_str>b_str) return a;
    else return b;
}
else if(a.type()==typeid(int) && b.type()==typeid(int)){
    int a_int=boost::any_cast<int>(a);
    int b_int=boost::any_cast<int>(b);
    if(a_int==b_int) return "None";
    if(a_int>b_int) return a;
    else return b;
}
else if(a.type()==typeid(int) && b.type()==typeid(string)){
    int a_int=boost::any_cast<int>(a);
    string b_str=boost::any_cast<string>(b);
    if(a_int==stoi(b_str)) return "None";
    if(a_int>stoi(b_str)) return a;
    else return b;
}
else if(a.type()==typeid(string) && b.type()==typeid(int)){
    string a_str=boost::any_cast<string>(a);
    int b_int=boost::any_cast<int>(b);
    if(stoi(a_str)==b_int) return "None";
    if(stoi(a_str)>b_int) return a;
    else return b;
}
else{
    float a_flt=boost::any_cast<float>(a);
    float b_flt=boost::any_cast<float>(b);
    if(a_flt==b_flt) return "None";
    if(a_flt>b_flt) return a;
    else return b;
}

}























