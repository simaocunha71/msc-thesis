class Solution {
public:
    string strongestExtension(string class_name, vector<string>& extensions) {
        int maxStrength = INT_MIN;
        string strongestExtension = "";

        for (const string& extension : extensions) {
            int strength = 0;
            for (char c : extension) {
                if (isupper(c)) {
                    strength++;
                } else if (islower(c)) {
                    strength--;
                }
            }
            if (strength > maxStrength) {
                maxStrength = strength;
                strongestExtension = extension;
            }
        }

        return class_name + "." + strongestExtension;
    }
};
