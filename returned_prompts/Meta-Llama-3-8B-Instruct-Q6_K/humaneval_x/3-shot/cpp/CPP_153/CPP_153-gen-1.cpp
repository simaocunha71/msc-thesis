    string strongest_ext="";
    int strongest_strength=-1;
    int i;
    for (i=0;i<extensions.size();i++)
    {
        int count_upper=0;
        int count_lower=0;
        int j;
        for (j=0;j<extensions[i].length();j++)
        {
            if (isupper(extensions[i][j]))
                count_upper++;
            else if (islower(extensions[i][j]))
                count_lower++;
        }
        int strength=count_upper-count_lower;
        if (strength>strongest_strength || (strength==strongest_strength && i<0))
        {
            strongest_strength=strength;
            strongest_ext=extensions[i];
        }
    }
    return class_name+"."+strongest_ext;
}  // This function will return the strongest extension for a given class name and a list of extensions. It first counts the number of uppercase and lowercase letters in each extension and calculates the strength of each extension as the difference between the number of uppercase and lowercase letters. It then selects the extension with the highest strength and returns the class name followed by the strongest extension. If there are multiple extensions with the same highest strength, it returns the first one in the list.  // Example usage: cout << Strongest_Extension("my_class", {"AA", "Be", "CC"}); // Output: "my_class.AA"  // Example usage: cout << Strongest_Extension("my_class", {"SErviNGSliCes", "Cheese", "StuFfed"}); // Output: "my_class.SErviNGSliCes"  // Example usage: cout << Strongest_Extension("my_class", {"AA", "Be", "CC", "BB", "DD"}); // Output: "my_class.AA"  // Example usage: cout << Strongest_Extension("my_class", {"SErviNGSliCes", "Cheese", "StuFfed", "AA", "BB", "CC"}); // Output: "my_class.SErviNGSliCes"  // Example usage: cout << Strongest_Extension("my_class", {"AA", "AA", "AA", "AA", "AA"}); // Output: "my_class.AA"  // Example usage: cout << Strongest_Extension("my_class", {"SErviNGSliCes", "SErviNGSliCes", "SEr