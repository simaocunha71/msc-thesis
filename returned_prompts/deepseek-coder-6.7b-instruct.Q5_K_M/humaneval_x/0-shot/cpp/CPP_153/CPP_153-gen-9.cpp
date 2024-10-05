    int CAP, SM;
    double strength, max_strength = -2;
    string strongest_extension;
    for (auto ext : extensions) {
        CAP = SM = 0;
        for (char c : ext) {
            if (isupper(c)) CAP++;
            if (islower(c)) SM++;
        }
        strength = (double)CAP - SM;
        if (strength > max_strength) {
            max_strength = strength;
            strongest_extension = ext;
        }
    }
    return class_name + '.' + strongest_extension;
}
int main(){
    printf("%s",Strongest_Extension("my_class", {"AA", "Be", "CC"}).c_str());
    return 0;
}

*/

*/
/*
