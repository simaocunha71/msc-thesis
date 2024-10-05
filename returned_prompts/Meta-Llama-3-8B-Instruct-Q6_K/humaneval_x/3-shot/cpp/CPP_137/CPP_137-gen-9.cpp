    if (a.type() != b.type())
    {
        if (a.type() == typeid(float) || a.type() == typeid(int))
        {
            if (b.type() == typeid(float) || b.type() == typeid(int))
            {
                float fa = boost::any_cast<float>(a);
                float fb = boost::any_cast<float>(b);
                if (fa > fb)
                {
                    return a;
                }
                else if (fa < fb)
                {
                    return b;
                }
                else
                {
                    return boost::any("None");
                }
            }
            else
            {
                string bs = boost::any_cast<string>(b);
                float fb = stol(bs.replace(",", ""));
                if (fa > fb)
                {
                    return a;
                }
                else if (fa < fb)
                {
                    return b;
                }
                else
                {
                    return boost::any("None");
                }
            }
        }
        else
        {
            string as = boost::any_cast<string>(a);
            float fa = stof(as.replace(",", ""));
            string bs = boost::any_cast<string>(b);
            float fb = stol(bs.replace(",", ""));
            if (fa > fb)
            {
                return a;
            }
            else if (fa < fb)
            {
                return b;
            }
            else
            {
                return boost::any("None");
            }
        }
    }
    else
    {
        float fa = boost::any_cast<float>(a);
        float fb = boost::any_cast<float>(b);
        if (fa > fb)
        {
            return a;
        }
        else if (fa < fb)
        {
            return b;
        }
        else
        {
            return boost::any("None");
        }
    }
}  //  END FUNCTION DEFINITION
BOOST_FOREACH(const auto& v, vector<int>){} //  END BOOST_FOREACH
int main() {
    //  TEST THE FUNCTION
    boost::any a = 1;
    boost::any b = 2.5;
    std::cout << boost::any_cast<string>(compare_one(a, b)) << std::endl;
    a = "5,1";
    b = 6;
    std::cout << boost::any_cast<string>(compare_one(a, b)) << std::endl;
    a = 1;
    b = 1;
    std::cout << boost::any_cast