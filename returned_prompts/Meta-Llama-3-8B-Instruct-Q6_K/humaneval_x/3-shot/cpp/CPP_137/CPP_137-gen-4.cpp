    if (a.type()==b.type())
    {
        if (a.type()==type<void*>())
        {
            string s1=any_cast<string>(a);
            string s2=any_cast<string>(b);
            if (s1.size()>0 && s2.size()>0)
            {
                float f1=stof(s1);
                float f2=stof(s2);
                if (f1>f2)
                    return a;
                else if (f1<f2)
                    return b;
                else
                    return boost::any("None");
            }
            else
                return boost::any("None");
        }
        else
        {
            float f1=any_cast<float>(a);
            float f2=any_cast<float>(b);
            if (f1>f2)
                return a;
            else if (f1<f2)
                return b;
            else
                return boost::any("None");
        }
    }
    else
    {
        if (a.type()==type<void*>())
        {
            string s1=any_cast<string>(a);
            float f2=any_cast<float>(b);
            if (stof(s1)>f2)
                return a;
            else if (stof(s1)<f2)
                return b;
            else
                return boost::any("None");
        }
        else
        {
            float f1=any_cast<float>(a);
            string s2=any_cast<string>(b);
            if (f1>stof(s2))
                return a;
            else if (f1<stof(s2))
                return b;
            else
                return boost::any("None");
        }
    }
}#include<boost/any.hpp>
using namespace std;
boost::any compare_one(boost::any a,boost::any b){
    if (a.type()==b.type())
    {
        if (a.type()==type<void*>())
        {
            string s1=any_cast<string>(a);
            string s2=any_cast<string>(b);
            if (s1.size()>0 && s2.size()>0)
            {
                float f1=stof(s1);
                float f2=stof(s2);
                if (f1>f2)
                    return a;
                else if (f1<f2)
                    return b;
                else
                    return boost::any("None");
            }
            else
                return boost::any("