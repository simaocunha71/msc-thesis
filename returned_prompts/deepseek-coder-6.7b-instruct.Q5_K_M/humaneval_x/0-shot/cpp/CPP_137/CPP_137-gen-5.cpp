    if (a.type() != typeid(b))
        return "Type mismatch";

B:
    switch (a.type().hash_code())
    {
    case typeid(int).hash_code():
        return boost::any_cast<int>(a) > boost::any_cast<int>(b) ? boost::any_cast<int>(a) : boost::any_cast<int>(b);
    case typeid(float).hash_code():
        return boost::any_cast<float>(a) > boost::any_cast<float>(b) ? boost::any_cast<float>(a) : boost::any_cast<float>(b);
    case typeid(string).hash_code():
        return boost::any_cast<string>(a) > boost::any_cast<string>(b) ? boost::any_cast<string>(a) : boost::any_cast<string>(b);
    default:
        return "None";
    }
}
int main() {
    printf("%f\n", boost::any_cast<float>(compare_one(1, 2.5)));
    printf("%s\n", boost::any_cast<const char*>(compare_one(1, "2.3")).c_str());
    printf("%s\n", boost::any_cast<const char*>(compare_one("5.1", "6")).c_str());
    printf("%s\n", boost::any_cast<const char*>(compare_one("1", 1)).c_str());
    return 0;
}
*/

int main() {
    printf("%f\n", boost::any_cast<float>(compare_one(1, 2.5)));
    printf("%s\n", boost::any_cast<const char*>(compare_one(1, "2.3")).c_str());
    printf("%s\n", boost::any_cast<const char*>(compare_one("5.1", "6")).c_str());
    printf("%s\n", boost::any_cast<const char*>(compare_