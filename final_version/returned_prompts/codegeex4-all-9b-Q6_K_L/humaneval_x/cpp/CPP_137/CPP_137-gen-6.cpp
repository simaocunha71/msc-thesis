#include<stdio.h>
#include<string>
#include<algorithm>
#include<boost/any.hpp>
using namespace std;

class Compare{
public:
    boost::any compare_one(boost::any a,boost::any b){
        boost::any c;
        if(a.type() == typeid(string)){
            string aa = boost::any_cast<string>(a);
            boost::algorithm::replace_all(aa, ",", ".");
            c = aa;
        }else{
            c = a;
        }
        if(b.type() == typeid(string)){
            string bb = boost::any_cast<string>(b);
            boost::algorithm::replace_all(bb, ",", ".");
            c = bb;
        }else{
            c = b;
        }
        if(c.type() == typeid(string)){
            string cc = boost::any_cast<string>(c);
            if(aa < bb){
                c = b;
            }else{
                c = a;
            }
        }else{
            double aa = boost::any_cast<double>(a);
            double bb = boost::any_cast<double>(b);
            if(aa < bb){
                c = b;
            }else{
                c = a;
            }
        }
        if(c.type() == typeid(string)){
            string cc = boost::any_cast<string>(c);
            if(aa == bb){
                return "None";
            }
            return c;
        }else{
            double aa = boost::any_cast<double>(a);
            double bb = boost::any_cast<double>(b);
            if(aa == bb){
                return "None";
            }
            return c;
        }
    }
};

int main(){
    Compare c;
    printf("%s\n",c.compare_one(1,2).c_str());
}

B:
#include<stdio.h>
#include<string>
#include<algorithm>
#include<boost/any.hpp>
using namespace std;

class Compare{
public:
    boost::any compare_one(boost::any a,boost::any b){
        boost::any c;
        if(a.type() == typeid(string)){
            string aa = boost::any_cast<string>(a);
            boost::algorithm::replace_all(aa, ",", ".");
            c = aa;
        }else{
            c = a;
        }
        if(b.type() == typeid(string)){
            string bb = boost::any_cast<string>(b);
            boost::algorithm::replace_all(bb, ",", ".");
            c = bb;
        }else{
            c = b;
        }
        if(c.type() == typeid(string)){
            string cc = boost::any