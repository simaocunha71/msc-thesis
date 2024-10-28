```c
#include <stdlib.h>
#include <string.h>

typedef struct Buffer {
    char* data;
    size_t size;
} Buffer;

Buffer copy_buffer(size_t n, Buffer* list) {
    Buffer result;
    size_t total_size = 0;
    Buffer* curr = list;

    while (curr != NULL && n > 0) {
        total_size += curr->size;
        curr = curr->next;
    }

    result.data = Buffer.allocUnsafe(total_size);
    result.size = total_size;

    curr = list;
    size_t offset = 0;

    while (curr != NULL && n > 0) {
        size_t copy_size = curr->size;
        if (copy_size > n) {
            copy_size = n;
        }

        memcpy(result.data + offset, curr->data, copy_size);
        offset += copy_size;
        curr = curr->next;
        n -= copy_size;
    }

    return result;
}
```