    vector<string> v;
    if(planet1=="Mercury"||planet2=="Mercury")
        goto B;
    if(planet1=="Venus"||planet2=="Venus")
        goto C;
    if(planet1=="Earth"||planet2=="Earth")
        goto D;
    if(planet1=="Mars"||planet2=="Mars")
        goto E;
    if(planet1=="Jupiter"||planet2=="Jupiter")
        goto F;
    if(planet1=="Saturn"||planet2=="Saturn")
        goto G;
    if(planet1=="Uranus"||planet2=="Uranus")
        goto H;
    if(planet1=="Neptune"||planet2=="Neptune")
        goto I;
    return v;
B:
    if(planet2=="Venus")
        goto C;
    else
        goto A;
C:
    if(planet2=="Earth")
        goto D;
    else
        goto B;
D:
    if(planet2=="Mars")
        goto E;
    else
        goto C;
E:
    if(planet2=="Jupiter")
        goto F;
    else
        goto D;
F:
    if(planet2=="Saturn")
        goto G;
    else
        goto E;
G:
    if(planet2=="Uranus")
        goto H;
    else
        goto F;
H:
    if(planet2=="Neptune")
        goto I;
    else
        goto G;
I:
    v.push_back(planet1);
    v.push_back(planet2);
    return v;
}

int main(){
    string planet1,planet2;
    vector<string> v;
    printf("Enter first planet name: ");
    scanf("%s",planet1);
   