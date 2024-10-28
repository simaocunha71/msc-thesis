    boost::any result;
    float fa = boost::any_cast<float>(a);
    float fb = boost::any_cast<float>(b);
    if (fa > fb){
        result = a;
    }
    else if (fa < fb){
        result = b;
    }
    else {
        result = boost::any("None");
    }
    return result;
}
// or
#include<boost/any.hpp>
#include<string>
using namespace std;
boost::any compare_one(boost::any a,boost::any b){
    boost::any result;
    if (boost::any_cast<float>(a) > boost::any_cast<float>(b)){
        result = a;
    }
    else if (boost::any_cast<float>(b) > boost::any_cast<float>(a)){
        result = b;
    }
    else {
        result = boost::any("None");
    }
    return result;
}  



