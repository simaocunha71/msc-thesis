    if (a.type() != b.type()){
        throw std::runtime_error("Types are not same");
    }
    else{
        if (a.type() == typeid(int)){
            int a1 = boost::any_cast<int>(a);
            int b1 = boost::any_cast<int>(b);
            if(a1 == b1) return "None";
            return max(a1, b1);
        }
        else if (a.type() == typeid(float)){
            float a1 = boost::any_cast<float>(a);
            float b1 = boost::any_cast<float>(b);
            if(a1 == b1) return "None";
            return max(a1, b1);
        }
        else if (a.type() == typeid(string)){
            string a1 = boost::any_cast<string>(a);
            string b1 = boost::any_cast<string>(b);
            a1.erase(remove(a1.begin(), a1.end(), ','), a1.end());
            b1.erase(remove(b1.begin(), b1.end(), ','), b1.end());
            float a_float = stof(a1);
            float b_float = stof(b1);
            if(a_float == b_float) return "None";
            return to_string(max(a_float, b_float));
        }
    }
}


