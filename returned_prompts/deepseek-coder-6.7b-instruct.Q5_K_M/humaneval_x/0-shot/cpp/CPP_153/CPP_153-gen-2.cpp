
    int max_strength = -1000000;
    string strongest_extension = "";
    for (auto extension : extensions) {
        int cap = 0, sm = 0;
        for (auto c : extension) {
            if (isupper(c)) cap++;
            if (islower(c)) sm++;
        }
        int strength = cap - sm;
        if (strength > max_strength) {
            max_strength = strength;
            strongest_extension = extension;
        }
    }

    return class_name + "." + strongest_extension;
}
*/




int main(){
    printf("Testing...\n");
    printf("Expected: my_class.AA\n");
    printf("Actual  : %s\n", Strongest_Extension("my_class", {"AA", "Be", "CC"}).c_str());
    printf("Expected: Slices.SErviNGSliCes\n");
    printf("Actual  : %s\n", Strongest_Extension("Slices", {"SErviNGSliCes", "Cheese", "StuFfed"}).c_str());
    printf("Expected: my_other_class.StuFfed\n");
    printf("Actual  : %s\n", Strongest_Extension("my_other_class", {"Cheese", "StuFfed"}).c_str());
    printf("Expected: yet_another_class.Cheese\n");
    printf("Actual  : %s\n", Strongest_Extension("yet_another_class", {"Cheese", "StuFfed"}).c_str());

    return 0;
}
/*
The function Strongest_Extension takes as arguments a string class_name and a vector of strings extensions. It loops through the vector of extensions and for each extension, it calculates the strength by subtracting the number of lowercase letters from the number of uppercase letters. If the strength of the current extension is greater than the previously stored max_strength, the function updates max_strength and strongest_extension. Finally, the function returns a string in the format "ClassName.StrongestExtension