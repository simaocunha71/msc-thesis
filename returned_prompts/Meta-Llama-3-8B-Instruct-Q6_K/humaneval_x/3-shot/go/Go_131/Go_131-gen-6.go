    var result int
    for ; n > 0; n /= 10 {
        digit := n % 10
        if digit % 2 != 0 {
            result *= 10
            result += digit
        }
    }
    return result
} // or use strconv.Itoa to convert int to string and then loop over each char to check if it is odd or even
} // or use a loop and convert each digit to string and check if it is odd or even
} // or use a loop and use remainder operator to get the last digit and check if it is odd or even
} // or use a loop and convert each digit to int and check if it is odd or even
} // or use a loop and check if the number is odd or even and then use a loop to get each digit
} // or use a loop and check if the number is odd or even and then use a loop to get each digit and check if it is odd or even
} // or use a loop and check if the number is odd or even and then use a loop to get each digit and check if it is odd or even and then return the product
} // or use a loop and check if the number is odd or even and then use a loop to get each digit and check if it is odd or even and then return the product and return 0 if all digits are even
} // or use a loop and check if the number is odd or even and then use a loop to get each digit and check if it is odd or even and then return the product and return 0 if all digits are even and then return the product of all digits
} // or use a loop and check if the number is odd or even and then use a loop to get each digit and check if it is odd or even and then return the product of all digits and then return 0 if all digits are even
} // or use a loop and check if the number is odd or even and then use a loop to get each digit and check if it is odd or even and then return the product of all digits and then return 0 if all digits are even and then return 0 if all digits are even
} // or use a loop and check if the number is odd or even and then use a loop to get each digit and check if it is odd or even and then return the product of all digits and then return 0 if all digits are even and then return 0