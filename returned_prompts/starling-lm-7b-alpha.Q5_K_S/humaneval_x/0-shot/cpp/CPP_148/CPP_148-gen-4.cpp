    vector<string> planets;
    if(planet1=="Mercury"||planet1=="Venus"||planet1=="Earth"||planet1=="Mars"||planet1=="Jupiter"||planet1=="Saturn"||planet1=="Uranus"||planet1=="Neptune"){
        if(planet2=="Mercury"||planet2=="Venus"||planet2=="Earth"||planet2=="Mars"||planet2=="Jupiter"||planet2=="Saturn"||planet2=="Uranus"||planet2=="Neptune"){
            planets.push_back("Mercury");
            planets.push_back("Venus");
            planets.push_back("Earth");
            planets.push_back("Mars");
            planets.push_back("Jupiter");
            planets.push_back("Saturn");
            planets.push_back("Uranus");
            planets.push_back("Neptune");
        }else{
            goto A;
        }
    }else{
        goto A;
    }
    int j=0;
    while(planets[j]!=planet1){
        j++;
    }
    int i=j;
    while(planets[i]!=planet2){
        i++;
    }
    vector<string> result;
    for(int k=j;k<i;k++){
        result.push_back(planets[k]);
    }
    return result;
}



int main(){
    vector<string> v=bf("Mercury","Neptune");
    for(int i=0;i<v.size();i++){
        printf("%s\n",v[i].c_str());
    }
    return 0;
}
























































