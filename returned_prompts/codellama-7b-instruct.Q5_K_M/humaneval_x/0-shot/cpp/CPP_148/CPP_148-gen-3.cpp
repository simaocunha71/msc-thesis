    vector<string> result;
    if(planet1=="Sun"||planet2=="Sun"){
        return result;
    }
    if(planet1=="Earth"||planet2=="Earth"){
        result.push_back("Earth");
        return result;
    }
    if(planet1=="Mercury"&&planet2=="Venus"){
        result.push_back("Mercury");
        result.push_back("Venus");
        return result;
    }
    if(planet1=="Venus"&&planet2=="Mars"){
        result.push_back("Venus");
        result.push_back("Mars");
        return result;
    }
    if(planet1=="Mars"&&planet2=="Jupiter"){
        result.push_back("Mars");
        result.push_back("Jupiter");
        return result;
    }
    if(planet1=="Jupiter"&&planet2=="Saturn"){
        result.push_back("Jupiter");
        result.push_back("Saturn");
        return result;
    }
    if(planet1=="Saturn"&&planet2=="Uranus"){
        result.push_back("Saturn");
        result.push_back("Uranus");
        return result;
    }
    if(planet1=="Uranus"&&planet2=="Neptune"){
        result.push_back("Uranus");
        result.push_back("Neptune");
        return result;
    }
    if(planet1=="Venus"&&planet2=="Earth"){
        result.push_back("Venus");
        result.push_back("Earth");
        return result;
    }
    if(planet1=="Mercury"&&planet2=="Uranus"){
        result.push_back("Mercury");
        result.push_back("Venus");
        result.push_back("Earth");
        result.push_back("M