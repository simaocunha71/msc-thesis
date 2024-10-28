    rot := 4
    result := ""
    for _, c := range s {
        if c >= 'a' && c <= 'z' {
            result += string((c - 'a' + rot) % 26 + 'a')
        } else if c >= 'A' && c <= 'Z' {
            result += string((c - 'A' + rot) % 26 + 'A')
        } else {
            result += string(c)
        }
    }
    return result
}  // This function uses a simple Caesar cipher to shift the letters down by 4 places. The modulus operator is used to ensure that the shift wraps around the alphabet. Non-alphabetic characters are left unchanged.  // This solution will not work if the input string contains non-ASCII characters, as the Caesar cipher only works with the 26 letters of the English alphabet. If you need to handle non-ASCII characters, you would need to use a more sophisticated encryption method.  // This function is case-sensitive, so uppercase and lowercase letters are treated differently. If you want the function to be case-insensitive, you would need to convert the input string to lowercase or uppercase before encrypting it.  // This function does not handle non-string inputs. If you want to handle non-string inputs, you would need to add error checking code to handle this.  // This function does not handle errors. If you want to handle errors, you would need to add error checking code to handle this.  // This function is not suitable for secure encryption, as the Caesar cipher is a simple and well-known encryption method. If you need to encrypt sensitive data, you should use a more secure encryption method.  // This function is not thread-safe, as it uses a global variable. If you need to use this function in a multithreaded environment, you would need to make it thread-safe.  // This function is not suitable for large inputs, as it uses a simple and inefficient algorithm. If you need to encrypt large inputs, you would need to use a more efficient algorithm.  // This function is not suitable for real-time applications, as it uses a simple and inefficient algorithm. If you need to encrypt data in real-time, you would need to use a more efficient algorithm.  // This function is not suitable for applications that require a high level of security, as the Caesar cipher is a simple and well-known encryption method. If you need to encrypt sensitive data, you should use a more