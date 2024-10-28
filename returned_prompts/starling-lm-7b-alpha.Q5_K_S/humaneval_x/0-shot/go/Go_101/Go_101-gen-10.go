The reason we need to import the "strings" package in the WordsString function is because the Fields function is a function in the "strings" package, and in order to use it, we need to import the "strings" package.

In Go, when you call a function, the compiler needs to know where to find the function and what it does. If a function is defined in another package, you need to import that package to use it.

In the example you gave, the Add function is defined in the "math" package, so you need to import the "math" package to use it. But in the WordsString function, the Fields function is defined in the "strings" package, so you need to import the "strings" package to use it.

If you don't import the "strings" package in the WordsString function, the compiler won't be able to find the Fields function and you will get a compilation error.

Therefore, in order to