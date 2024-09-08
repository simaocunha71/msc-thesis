    int max_strength = -1000000;
    string strongest_extension;
    for (int i = 0; i < extensions.size(); i++) {
        int cap = 0, sm = 0;
        for (int j = 0; j < extensions[i].size(); j++) {
            if (isupper(extensions[i][j]))
                cap++;
            else
                sm++;
        }
        int strength = cap - sm;
        if (strength > max_strength) {
            max_strength = strength;
            strongest_extension = extensions[i];
        }
    }
    return class_name + "." + strongest_extension;
}

int main() {
    string className = "Slices";
    vector<string> extensions = {"SErviNGSliCes", "Cheese", "StuFfed"};
    printf("%s\n",Strongest_Extension(className,extensions).c_str());
    return 0;
}
