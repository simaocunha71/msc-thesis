    vector<string> all_planets={"Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"};
    vector<string> between_planets;
    int i;
    int j;
    string planet1_index;
    string planet2_index;
    for (i=0;i<all_planets.size();i++){
        if (all_planets[i]==planet1)
        planet1_index=to_string(i);
        if (all_planets[i]==planet2)
        planet2_index=to_string(i);
    }
    if (planet1_index=="-1"||planet2_index=="-1"){
        return {};
    }
    int planet1_index_int=stoi(planet1_index);
    int planet2_index_int=stoi(planet2_index);
    if (planet1_index_int<planet2_index_int){
        for (i=planet1_index_int;i<planet2_index_int;i++){
            between_planets.push_back(all_planets[i]);
        }
    }
    else{
        for (i=planet1_index_int;i<8;i++){
            between_planets.push_back(all_planets[i]);
        }
        for (j=0;j<planet2_index_int;j++){
            between_planets.push_back(all_planets[j]);
        }
    }
    return between_planets;
}



