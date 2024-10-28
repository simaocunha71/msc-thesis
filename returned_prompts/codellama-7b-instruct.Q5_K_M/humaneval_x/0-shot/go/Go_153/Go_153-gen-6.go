import (
    "math"
    "strings"
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
    // Write your code here.
    if len(extensions) == 0 {
        return class_name
    }
    class_name = strings.ToUpper(class_name)
    strongest := -1
    strongest_name := ""
    for _, extension := range extensions {
        extension = strings.ToUpper(extension)
        cap := 0
        sm := 0
        for _, char := range extension {
            if unicode.IsLetter(char) {
                if unicode.IsUpper(char) {
                    cap += 1
                } else {
                    sm += 1
                }
            }
        }
        strength := float64(cap - sm)
        if strength > strongest {
            strongest = int(strength)
            strongest_name = extension
        } else if strength == strongest && len(extension