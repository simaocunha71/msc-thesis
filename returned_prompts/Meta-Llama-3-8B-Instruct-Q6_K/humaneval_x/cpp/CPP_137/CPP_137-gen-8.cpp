boost::any a = boost::any(a);
boost::any b = boost::any(b);

if(a.type() == typeid(int) && b.type() == typeid(int)){
    int x = boost::any_cast<int>(a);
    int y = boost::any_cast<int>(b);
    return (x > y) ? a : (x < y) ? b : boost::any("None");
}
else if(a.type() == typeid(float) && b.type() == typeid(float)){
    float x = boost::any_cast<float>(a);
    float y = boost::any_cast<float>(b);
    return (x > y) ? a : (x < y) ? b : boost::any("None");
}
else if(a.type() == typeid(string) && b.type() == typeid(string)){
    string x = boost::any_cast<string>(a);
    string y = boost::any_cast<string>(b);
    if(stoi(x) > stoi(y)) return a;
    else if(stoi(y) > stoi(x)) return b;
    else return boost::any("None");
}
else return boost::any("Error");

}

int main(){
    cout<<boost::any_cast<boost::any>(compare_one(1, 2.5))<<endl;
    cout<<boost::any_cast<boost::any>(compare_one(1, "2,3"))<<endl;
    cout<<boost::any_cast<boost::any>(compare_one("5,1", "6"))<<endl;
    cout<<boost::any_cast<boost::any>(compare_one("1", 1))<<endl;
    return 0;
}

