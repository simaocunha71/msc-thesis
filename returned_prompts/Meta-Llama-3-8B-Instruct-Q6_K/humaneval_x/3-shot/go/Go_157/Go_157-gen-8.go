    if a*a+b*b==c*c || a*a+c*c==b*b || b*b+c*c==a*a {
        return true
    }
    return false
}  // This function checks if the given sides can form a right-angled triangle. It does this by using the Pythagorean theorem. If the sum of the squares of any two sides is equal to the square of the third side, then they can form a right-angled triangle. If not, it returns false.