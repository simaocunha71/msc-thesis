    if(typeid(a)!=typeid(b)){
        if(typeid(a)==typeid(int)){
            if(typeid(b)==typeid(float) || typeid(b)==typeid(double)){
                if(a<b)
                    return b;
                else
                    return a;
            }
            else if(typeid(b)==typeid(string)){
                int x = boost::any_cast<int>(a);
                string s = boost::any_cast<string>(b);
                int y = atoi(s.c_str());
                if(x<y)
                    return s;
                else
                    return x;
            }
        }
        else if(typeid(a)==typeid(float) || typeid(a)==typeid(double)){
            if(typeid(b)==typeid(int)){
                double x = boost::any_cast<double>(a);
                int y = boost::any_cast<int>(b);
                if(x<y)
                    return y;
                else
                    return x;
            }
            else if(typeid(b)==typeid(string)){
                double x = boost::any_cast<double>(a);
                string s = boost::any_cast<string>(b);
                int y = atoi(s.c_str());
                if(x<y)
                    return s;
                else
                    return x;
            }
        }
        else if(typeid(a)==typeid(string)){
            if(typeid(b)==typeid(int)){
                string s = boost::any_cast<string>(a);
                int y = boost::any_cast<int>(b);
                if(atoi(s.c_str())<y)
                    return y;
                else
                    return s;
            }
            else if(typeid(b)==typeid(float) || typeid(b)==typeid(double)){
                string s = boost::any_