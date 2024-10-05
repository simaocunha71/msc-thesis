
1. Use <cmath> instead of <math.h>
You are using the C++ header math.h, which is a C header. Instead, use the C++ header cmath. The C++ standard library has a more modern and feature-complete math library, which is the one you should use.
#include <cmath>

2. Use <algorithm> for std::abs
You are using the abs function from the C standard library. This is not a good idea. Instead, use the std::abs function from the C++ standard library. The abs function from the C++ standard library has the same functionality as the abs function from the C standard library, but it is more convenient to use.
#include <algorithm>

3. Use <iostream> instead of <stdio.h>
You are using the C standard input/output library, which is not a good idea. Instead, use the C++ standard input/output library. The C++ standard input/output library has a more modern and feature-complete I/O library, which is the one you should use.
#include <iostream>

4. Use std::vector instead of std::vector
You are using the std::vector template from the C++ standard library. This is a good idea. The std::vector template is a convenient and powerful container for dynamic arrays.
#include <vector>

5. Use std::string instead of std::string
You are using the std::string template from the C++ standard library. This is a good idea. The std::string template is a convenient and powerful container for strings.
#include <string>

6. Use std::cout instead of std::printf
You are using the printf function from the C standard library. This is not a good idea. Instead, use the std::cout object from the C++ standard library