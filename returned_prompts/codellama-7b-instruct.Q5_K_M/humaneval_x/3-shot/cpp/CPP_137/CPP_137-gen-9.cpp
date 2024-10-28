    if (a.type()==b.type()){
        if (a==b) return "None";
        if (a.type()==typeid(int))
        {
            if (a<b) return b;
            else return a;
        }
        if (a.type()==typeid(float))
        {
            if (a<b) return b;
            else return a;
        }
        if (a.type()==typeid(string))
        {
            string s1=boost::any_cast<string>(a);
            string s2=boost::any_cast<string>(b);
            replace_if(s1.begin(),s1.end(),',','.');
            replace_if(s2.begin(),s2.end(),',','.');
            float f1=stof(s1);
            float f2=stof(s2);
            if (f1<f2) return b;
            else return a;
        }
    }
}



