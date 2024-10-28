    var strongest_extension string
    strongest_extension_strength := -math.MaxFloat64

    for _, extension := range extensions {
        var strength float64
        for _, c := range extension {
            if c >= 'A' && c <= 'Z' {
                strength += 1
            } else if c >= 'a' && c <= 'z' {
                strength -= 1
            }
        }

        if strength > strongest_extension_strength {
            strongest_extension_strength = strength
            strongest_extension = extension
        }
    }

    return class_name + "." + strongest_extension
}  // end of StrongestExtension
// Test cases
// 1. Test with a class name and extensions.
//  test("StrongestExtension", func() {
//     assert("my_class.AA", StrongestExtension("my_class", []string{"AA", "Be", "CC"}))
//  })
// 2. Test with a class name and one extension.
//  test("StrongestExtension", func() {
//     assert("my_class.AA", StrongestExtension("my_class", []string{"AA"}))
//  })
// 3. Test with a class name and no extensions.
//  test("StrongestExtension", func() {
//     assert("", StrongestExtension("my_class", []string{}))
//  })  // end of test cases
// 4. Test with a class name and multiple extensions with the same strength.
//  test("StrongestExtension", func() {
//     assert("my_class.AA", StrongestExtension("my_class", []string{"AA", "AA", "CC"}))
//  })  // end of test cases
// 5. Test with a class name and multiple extensions with different strengths.
//  test("StrongestExtension", func() {
//     assert("my_class.AA", StrongestExtension("my_class", []string{"AA", "Be", "CC", "DD"}))
//  })  // end of test cases  // end of test cases
// 6. Test with a class name and one extension with zero strength.
//  test("StrongestExtension", func() {
//     assert("my_class.BE", StrongestExtension("my_class", []string{"Be"}))
//  })  // end of test cases
// 7. Test with a class name and multiple extensions with zero strength.
//  test("StrongestExtension", func() {
//