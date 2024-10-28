
First of all, I think you need to use the <cmath> header instead of <math.h> in the first two questions. The <cmath> header is a part of C++ standard and the <math.h> is a part of C standard.

Secondly, you do not need to use the namespace std in C++ programs. In fact, it is considered good practice to avoid using the namespace std in order to avoid name clashes.

Thirdly, the functions can be better named, and the variable names are not descriptive enough. For example, in the first function, the variable names i and j are not descriptive enough. Instead, you can use names like left and right. And, instead of calling the function has_close_elements, you can name it has_close_numbers.

Fourthly, in the third function, the variable name number is not descriptive enough. Instead, you can name it decimal_number.

Fifthly, in the fourth function, the variable name values is not descriptive enough. Instead, you can name it values_list.

Finally, the code is not indented properly. Make sure to indent the code properly.