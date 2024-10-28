    return x+y;
}

int main(){
    printf("%d\n",add(2,3));
    printf("%d\n",add(5,7));
    return 0;
}
\end{lstlisting}

\end{document}


A: The question is not very clear but if you're asking for a way to make comments in a code block, you can use the following syntax:

\begin{lstlisting}[language=C++, caption={A program in C++}, label=lst:first]
#include <iostream>
int main() {
    // This is a single-line comment
    std::cout << "Hello, World!";

    /*
    This is a
    multi-line comment
    */

    return 0;
}
\end{lstlisting}

This will create a listing of the code with a single-line comment and a multi-line comment. The single-line comment will be italicized, and the multi-line comment will be in a different color.

If you're asking for a way to make "Q" and "A" labels for code blocks, you can use the following syntax:

\begin{lstlisting}[language=C++, caption={A program in C++}, label=lst:first]
