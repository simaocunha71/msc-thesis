
The first function seems fine. It's a brute force solution, and it works.

The second function is also fine. It's not the most efficient, but it works.

The third function has a bug. The modulus operation should be done with a floating point number, not an integer. Otherwise, it will always return 0.0.

The fourth function is fine. It's a simple call to the built-in crypto library.