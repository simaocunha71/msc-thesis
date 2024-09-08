    int numeratorX = std::stoi(x.substr(0, x.find('/')));
    int denominatorX = std::stoi(x.substr(x.find('/') + 1));
    int numeratorN = std::stoi(n.substr(0, n.find('/')));
    int denominatorN = std::stoi(n.substr(n.find('/') + 1));

    // find the greatest common divisor of the two denominators
    int gcd = std::gcd(denominatorX, denominatorN);
    // simplify the fractions
    int numeratorXsimplified = numeratorX * (denominatorN / gcd);
    int denominatorXsimplified = denominatorX * (denominatorN / gcd);
    int numeratorNsimplified = numeratorN * (denominatorX / gcd);
    int denominatorNsimplified = denominatorN * (denominatorX / gcd);

    // check if the simplified fractions are equal
    if(numeratorXsimplified == numeratorNsimplified && denominatorXsimplified == denominatorNsimplified){
        return true;
    }
    return false;
}

int main(){
    printf("%s\n", (simplify("1/5", "5/1") ? "true" : "false"));  // true
    printf("%s\n", (simplify("1/6", "2/1") ? "true" : "false"));  // false
    printf("%s\n", (simplify("7/10", "10/2") ? "true" : "false")); // false
    return 0;
}
