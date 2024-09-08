    int max_strength = -INT_MAX;
    string strongest_extension;
    for (string ext : extensions) {
        int cap = 0, sm = 0;
        for (char c : ext) {
            if (isupper(c)) cap++;
            else if (islower(c)) sm++;
        }
        int strength = cap - sm;
        if (strength > max_strength) {
            max_strength = strength;
            strongest_extension = ext;
        }
    }
    return class_name + "." + strongest_extension;
}
int main()
{
    vector<string> extensions = {"AA", "Be", "CC"};
    string class_name = "my_class";
    cout << Strongest_Extension(class_name, extensions);
}
C:
    Output: my_class.AA
    Explanation: 
    This program iterates over the extensions and calculates the strength of each extension. 
    It keeps track of the strongest extension seen so far. 
    If it sees a stronger extension, it updates the strongest extension. 
    Finally, it returns the class name followed by the strongest extension. 
    In this example, the extensions are "AA", "Be", and "CC". 
    The strength of "AA" is 2-0 = 2, the strength of "Be" is 0-1 = -1, 
    and the strength of "CC" is 2-0 = 2. 
    Since "AA" and "CC" have the same strength, it chooses the one that comes first, which is "AA". 
    Therefore, the output is "my_class.AA". 
}
```



### Code Explanation:
The code defines a function `Strongest_Extension` that takes a class name and a vector of extensions as input. It then iterates over the extensions, calculates their strength (the number of uppercase letters minus the number of lowercase letters), and keeps track of the strongest extension seen so far. If it finds an extension with a higher strength, it updates the strongest extension. Finally, it returns the class name followed by the strongest extension.

In the `main` function, we create a vector of extensions `{"AA", "Be", "CC"}` and a class name `"my_class"`. We then call the `Strongest_Extension` function with these inputs and print the result.

The output of the program is `"my_class.AA"`, which is the class name followed by the strongest extension `"AA"`. This is because the