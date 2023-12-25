import (
    "math"
)

// You will be given the name of a class (a string) and a list of extensions.
// The extensions are to be used to load additional classes to the class. The
// strength of the extension is as follows: Let CAP be the number of the uppercase
// letters in the extension's name, and let SM be the number of lowercase letters
// in the extension's name, the strength is given by the fraction CAP - SM.
// You should find the strongest extension and return a string in this
// format: ClassName.StrongestExtensionName.
// If there are two or more extensions with the same strength, you should
// choose the one that comes first in the list.
// For example, if you are given "Slices" as the class and a list of the
// extensions: ['SErviNGSliCes', 'Cheese', 'StuFfed'] then you should
// return 'Slices.SErviNGSliCes' since 'SErviNGSliCes' is the strongest extension
// (its strength is -1).
// Example:
// for StrongestExtension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
func StrongestExtension(class_name string, extensions []string) string {
    // Add a suffix to the class name so that you will not pick it as an extension
    classname := strings.ToUpper(string(class_name)) + ".EX"
    strongestStrength := math.MaxInt64 - 1
    for _, ext := range extensions {
        extStrength, _ := findExtStrength(ext)
        if extStrength > strongestStrength {
            classname = strings.ToUpper(string(class_name)) + ".EX." + ext
            strongestStrength = extStrength
        }
    }
    return string(classname)
}

func findExtStrength(ext string) (strength int, err error) {
    for _, part := range strings.SplitAfter("_", ext) {
        if !strings.ContainsRune(part, 'S') && !strings.ContainsRune(part, 'C')