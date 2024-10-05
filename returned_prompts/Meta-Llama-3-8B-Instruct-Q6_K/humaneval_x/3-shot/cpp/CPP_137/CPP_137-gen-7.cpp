    boost::any result;
    double da=db=0.0;
    if (boost::any_cast<double>(a) > boost::any_cast<double>(b))
    {
        result=a;
    }
    else if (boost::any_cast<double>(b) > boost::any_cast<double>(a))
    {
        result=b;
    }
    else
    {
        result="None";
    }
    return result;
}
#include<boost/any.hpp>
#include<sstream>
#include<iomanip>
using namespace std;
string compare_one(boost::any a,boost::any b){
    boost::any result;
    double da=db=0.0;
    if (boost::any_cast<double>(a) > boost::any_cast<double>(b))
    {
        result=a;
    }
    else if (boost::any_cast<double>(b) > boost::any_cast<double>(a))
    {
        result=b;
    }
    else
    {
        result="None";
    }
    return boost::any_cast<string>(result);
}
#include<string>
#include<sstream>
#include<iomanip>
using namespace std;
string compare_one(string a,string b){
    double da=stod(a),db=stod(b);
    if (da > db)
    {
        return a;
    }
    else if (db > da)
    {
        return b;
    }
    else
    {
        return "None";
    }
}  // string compare_one(string a, string b) {
//     double da = stod(a), db = stod(b);
//     if (da > db)
//     {
//         return a;
//     }
//     else if (db > da)
//     {
//         return b;
//     }
//     else
//     {
//         return "None";
//     }
// }  // string compare_one(string a, string b) {
//     double da = stod(a), db = stod(b);
//     if (da > db)
//     {
//         return a;
//     }
//     else if (db > da)
//     {
//         return b;
//     }
//     else
//     {
//         return "None";
//     }
// }  // string compare_one(string a, string b) {
//     double da = stod(a), db = stod(b);
//     if (da > db)
//     {
//         return a;
//     }
//    