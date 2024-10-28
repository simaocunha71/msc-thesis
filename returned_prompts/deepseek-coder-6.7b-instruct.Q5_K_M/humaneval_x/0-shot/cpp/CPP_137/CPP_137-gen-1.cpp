
    string sa = boost::any_cast<string>(a);
    string sb = boost::any_cast<string>(b);
    replace(sa.begin(), sa.end(), ',', '.');
    replace(sb.begin(), sb.end(), ',', '.');
    float fa = stof(sa);
    float fb = stof(sb);
    
    int ia = stoi(sa);
    int ib = stoi(sb);
    
    if(fa > fb) return a;
    else if(fb > fa) return b;
    else if(ia > ib) return a;
    else if(ib > ia) return b;
    else return "None";
    
}
*/

int main()
{
    printf("%s\n", boost::any_cast<string>(compare_one(1, 2.5)).c_str());
    printf("%s\n", boost::any_cast<string>(compare_one(1, "2,3")).c_str());
    printf("%s\n", boost::any_cast<string>(compare_one("5,1", "6")).c_str());
    printf("%s\n", boost::any_cast<string>(compare_one("1", 1)).c_str());
    return 0;
}

/*
int main()
{
    printf("%f\n", boost::any_cast<float>(compare_one(1, 2.5)));
    printf("%s\n", boost::any_cast<string>(compare_one(1, "2,3")).c_str());
    printf("%s\n", boost::any_cast<string>(compare_one("5,1", "6")).c_str());
    printf("%s\n", boost::any_cast<string>(compare_one("1", 1)).c_str());
    return 0;
}
*/

//Test/compare_one.cpp
#define BOOST_TEST_DYN_LINK
#define BOOST_TEST_MODULE Main
#include <boost/test/unit_test.hpp>
#include "