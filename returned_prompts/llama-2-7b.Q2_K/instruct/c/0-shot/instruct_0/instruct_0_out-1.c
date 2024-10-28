*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct StringArray {
	char ** strings;
	int size;
};

void free(StringArray * array) {
    for (size_t i = 0; i < array->size; ++i) {
        if (array->strings[i]) {
            free(array->strings[i]);
        }
    }
}

int main()
{
	StringArray * arr;
	arr = malloc(sizeof(StringArray));
	if (!arr) { return -1; }

	// Allocate space for our new array.
	int size = 50;
	arr->size = size;
	arr->strings = malloc(size * sizeof(char*));

	for (int i=0; i<size; ++i) {
		arr->strings[i] = malloc(sizeof(char*) * strlen("Hello"));
    }
    free(arr);
}