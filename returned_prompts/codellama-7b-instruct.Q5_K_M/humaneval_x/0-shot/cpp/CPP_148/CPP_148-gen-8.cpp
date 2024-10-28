    if(planet1=="Mercury" && planet2=="Venus")
        return {"Venus"};
    else if(planet1=="Venus" && planet2=="Earth")
        return {"Venus", "Earth", "Mars", "Jupiter", "Saturn"};
    else if(planet1=="Earth" && planet2=="Mars")
        return {"Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus"};
    else if(planet1=="Mars" && planet2=="Jupiter")
        return {"Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
    else if(planet1=="Jupiter" && planet2=="Saturn")
        return {"Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
    else if(planet1=="Saturn" && planet2=="Uranus")
        return {"Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
    else if(planet1=="Uranus" && planet2=="Neptune")
        return {"Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
    else
        return {};

}
int main(){

    cout<<bf("Jupiter", "Neptune")[0]<<endl;
    cout<<bf("Earth", "Mercury")[0]<<endl;
    cout<<bf("Mercury", "Uranus")[0]<<endl;
    return 0;
}
