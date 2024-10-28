
```c
inline Buffer* copyBuffer(int n, Buffer* list) {
    Buffer* buffer = Buffer.allocUnsafe(n);
    for (Buffer* chunk = list; chunk != NULL; chunk = chunk->next) {
        if (chunk->length <= n) {
            chunk->copy(buffer, 0, n);
            n -= chunk->length;
        } else {
            chunk->copy(buffer, 0, n);
            buffer->length = n;
            break;
        }
    }
    return buffer;
}
```
