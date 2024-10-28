
C++ is a statically typed language, which means that the types of variables must be known at compile time. The types of the parameters and return types must be specified explicitly. This is why the vector and string types are included in the function signatures. The compiler needs to know the type of the elements that the vector contains, and the type of characters that the string contains. These types are specified explicitly in the function signatures.
The types of the variables and parameters must be known at compile time because C++ does not have a runtime type system. This means that the type of a variable cannot change during the execution of the program. The type of a variable is determined by its declaration, and cannot be changed later. This is why the types of the variables and parameters must be specified explicitly in the function signatures.
Also, you can use the auto keyword to let the compiler automatically deduce the type of the variable from its initializer. This can make the code more readable, and reduce the amount of code that needs to be written. For example, you can write:
auto i = 0;
auto j = 1;
auto threshold = 0.5;

instead of:
int i = 0;
int j = 1;
float threshold = 0.5;

This is because the types of the variables i and j are known from their initializers, so the compiler can deduce their types automatically.
In C++, the types of variables and parameters must be known at compile time, and cannot be changed during the execution of the program. The types of the variables and parameters must be specified explicitly in the function signatures, and the compiler needs to know the types of the elements that the vector and string types contain. The auto keyword can be used to let the compiler automatically deduce the type of a variable from its initializer.