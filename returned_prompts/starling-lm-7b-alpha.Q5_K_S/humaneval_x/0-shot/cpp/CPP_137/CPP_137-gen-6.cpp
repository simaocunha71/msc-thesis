if (boost::holds_alternative<float>(a) && boost::holds_alternative<float>(b)) {
    if (boost::get<float>(a) > boost::get<float>(b)) {
        return a;
    } else {
        return b;
    }

} else if (boost::holds_alternative<int>(a) && boost::holds_alternative<int>(b)) {
    if (boost::get<int>(a) > boost::get<int>(b)) {
        return a;
    } else {
        return b;
    }
} else if (boost::holds_alternative<std::string>(a) && boost::holds_alternative<std::string>(b)) {
    if (boost::get<std::string>(a) > boost::get<std::string>(b)) {
        return a;
    } else {
        return b;
    }
} else {
    return "None";
}
}

int main() {
    boost::any a = 2, b = 5;
    cout << compare_one(a, b) << endl;
    return 0;
}
















































































































































































































































