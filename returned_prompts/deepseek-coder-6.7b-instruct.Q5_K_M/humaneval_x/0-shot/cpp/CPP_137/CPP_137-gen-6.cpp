if(a.type() != typeid(b)){
    throw std::invalid_argument("Different types are not supported");
}

B:
if(a.type() == typeid(int)){
    int x = boost::any_cast<int>(a);
    int y = boost::any_cast<int>(b);
    if(x > y){
        return x;
    }
    if(x < y){
        return y;
    }
    return "None";
}

C:
if(a.type() == typeid(float)){
    float x = boost::any_cast<float>(a);
    float y = boost::any_cast<float>(b);
    if(x > y){
        return x;
    }
    if(x < y){
        return y;
    }
    return "None";
}

D:
if(a.type() == typeid(string)){
    string x = boost::any_cast<string>(a);
    string y = boost::any_cast<string>(b);
    x.erase(remove(x.begin(), x.end(), ','), x.end());
    y.erase(remove(y.begin(), y.end(), ','), y.end());

    float fx = stof(x);
    float fy = stof(y);
    if(fx > fy){
        return x;
    }
    if(fx < fy){
        return y;
    }
    return "None";
}
}

int main()
{
    boost::any a = 2.5;
    boost::any b = "2,3";
    cout<<compare_one(a, b);
    return 0;
}

Your code has some syntax errors and I'm not sure if it would work as expected. The boost::any library in C++ is not as flexible as that in Python, and it is not designed to be used in this way. The code you provided is not a complete solution.

I would suggest you to use the function templates or use the C++ type traits.

Here is the solution using function templates: