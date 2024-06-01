Write a function in C that takes an integer error code as input and returns a human-readable error message using the standard library function `gai_strerror()`.

    Only return the code, don't include any other information,
    such as a preamble or suffix.
*/

#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#define MAXLEN 1024
int error_code;
int main() {
	error_code = atoi(argv[1]);
	if (error_code == -1) return EXIT_FAILURE;
	printf("Error code %d: ", error_code);
    fprintf(stdout, gai_strerror(error_code));
}
