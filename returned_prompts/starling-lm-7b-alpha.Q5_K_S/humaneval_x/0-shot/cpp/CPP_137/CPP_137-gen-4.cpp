    if(boost::type<int>()(a) && boost::type<int>()(b)){
        if(a<b) return b;
        else return a;
    }
    else if(boost::type<float>()(a) && boost::type<float>()(b)){
        if(a<b) return b;
        else return a;
    }
    else if(boost::type<string>()(a) && boost::type<string>()(b)){
        if(a<b) return b;
        else return a;
    }
    else if(boost::type<int>()(a) && boost::type<string>()(b)){
        if(a<b) return a;
        else return b;
    }
    else if(boost::type<string>()(a) && boost::type<int>()(b)){
        if(a<b) return a;
        else return b;
    }
    else if(boost::type<float>()(a) && boost::type<string>()(b)){
        if(a<b) return a;
        else return b;
    }
    else if(boost::type<string>()(a) && boost::type<float>()(b)){
        if(a<b) return a;
        else return b;
    }
    else if(boost::type<string>()(a) && boost::type<string>()(b)){
        if(a<b) return a;
        else return b;
    }
    else if(boost::type<float>()(a) && boost::type<float>()(b)){
        if(a<b) return a;
        else return b;
    }
    else if(boost::type<int>()(a) && boost::type<string>()(b)){
        if(a<b) return a;
        else return b;
    }
    else if(boost::type<string>()(a) && boost::type<int>()(b)){
        if(a<b) return a;
        else return b;
    }
    else if(boost::type<float>()(a) && boost::type<int>()(b)){
        if(a<