    vector<string> all_planets;
    if (planet1=="Mercury")
    all_planets.push_back("Venus");
    else if (planet1=="Venus")
    all_planets.push_back("Earth");
    else if (planet1=="Earth")
    all_planets.push_back("Mars");
    else if (planet1=="Mars")
    all_planets.push_back("Jupiter");
    else if (planet1=="Jupiter")
    all_planets.push_back("Saturn");
    else if (planet1=="Saturn")
    all_planets.push_back("Uranus");
    else if (planet1=="Uranus")
    all_planets.push_back("Neptune");
    else
    return all_planets;

    if (planet2=="Venus")
    all_planets.push_back("Earth");
    else if (planet2=="Earth")
    all_planets.push_back("Mars");
    else if (planet2=="Mars")
    all_planets.push_back("Jupiter");
    else if (planet2=="Jupiter")
    all_planets.push_back("Saturn");
    else if (planet2=="Saturn")
    all_planets.push_back("Uranus");
    else if (planet2=="Uranus")
    all_planets.push_back("Neptune");
    else if (planet2=="Neptune")
    return all_planets;

    return all_planets;
}

