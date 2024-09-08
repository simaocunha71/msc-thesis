    int max_strength = -1000000; // Initialize the maximum strength
    string strongest_extension = ""; // Initialize the strongest extension

    for (const auto& extension : extensions) {
        int cap = 0; // Initialize the count of uppercase letters
        int sm = 0; // Initialize the count of lowercase letters
        for (char c : extension) {
            if (isupper(c)) {
                cap++;
            } else if (islower(c)) {
                sm++;
            }
        }
        int strength = cap - sm; // Calculate the strength
        if (strength > max_strength) {
            max_strength = strength;
            strongest_extension = extension;
        }
    }
    return class_name + "." + strongest_extension;
}
B:
    int main() {
        string class_name;
        vector<string> extensions;
        cout << "Enter the name of the class: ";
        cin >> class_name;
        cout << "Enter the extensions: ";
        int n;
        cin >> n;
        for (int i = 0; i < n; i++) {
            string extension;
            cin >> extension;
            extensions.push_back(extension);
        }
        cout << "The strongest extension for the class " << class_name << " is: " << Strongest_Extension(class_name, extensions) << endl;
        return 0;
    }
C:
    int main() {
        string class_name;
        vector<string> extensions;
        cout << "Enter the name of the class: ";
        cin >> class_name;
        cout << "Enter the extensions: ";
        int n;
        cin >> n;
        for (int i = 0; i < n; i++) {
            string extension;
            cin >> extension;
            extensions.push_back(extension);
        }
        cout << "The strongest extension for the class " << class_name << " is: " << Strongest_Extension(class_name, extensions) << endl;
        return 0;
    }
D:
    int main() {
        string class_name;
        vector<string> extensions;
        cout << "Enter the name of the class: ";
        cin >> class_name;
        cout << "Enter the extensions: ";
        int n;
        cin >> n;
        for (int i = 0; i < n; i++) {
            string extension;
            cin >> extension;
            extensions.push_back(extension);
        }
        cout << "The strongest extension for the class " << class_name << " is: