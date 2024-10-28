    // Create a dictionary to store the strength of each extension.
    strength := make(map[string]float64)

    // Iterate through each extension.
    for _, extension := range extensions {
        // Create a variable to store the strength of the current extension.
        cap, sm := 0, 0
        // Iterate through the characters of the current extension.
        for _, char := range extension {
            // If the character is an uppercase letter, increment cap.
            if char >= 'A' && char <= 'Z' {
                cap++
            }
            // If the character is a lowercase letter, increment sm.
            if char >= 'a' && char <= 'z' {
                sm++
            }
        }
        // Calculate the strength of the current extension.
        strength[extension] = float64(cap) - float64(sm)
    }

    // Create a variable to store the strongest extension.
    strongestExtension := ""
    // Create a variable to store the strength of the strongest extension.
    strongestStrength := -1.0
    // Iterate through the extensions.
    for _, extension := range extensions {
        // If the current extension's strength is stronger than the strongest, update the strongest and strongestExtension.
        if strength[extension] > strongestStrength {
            strongestStrength = strength[extension]
            strongestExtension = extension
        }
    }
    return class_name + "." + strongestExtension
}







































































































































































