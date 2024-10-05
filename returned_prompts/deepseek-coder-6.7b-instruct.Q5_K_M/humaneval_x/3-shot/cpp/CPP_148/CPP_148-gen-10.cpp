    vector<string> planets {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
    vector<string> result;
    int i,j;
    for(i=0;i<planets.size();i++){
        if(planets[i]==planet1){
            for(j=i+1;j<planets.size();j++){
                if(planets[j]==planet2){
                    for(int k=i+1;k<j;k++){
                        result.push_back(planets[k]);
                    }
                    return result;
                }
            }
        }
    }
    return result;
}


