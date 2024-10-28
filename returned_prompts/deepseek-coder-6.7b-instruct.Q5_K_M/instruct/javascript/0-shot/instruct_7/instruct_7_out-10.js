```c
buffer_t copy_buffered_data(size_t n, bufferlist_t list) {
    buffer_t new_buffer = Buffer.allocUnsafe(n);
    buffer_t current_buffer = list;

    while (n > 0 && current_buffer != NULL) {
        size_t chunk_size = min(n, current_buffer->length);
        memcpy(new_buffer->data, current_buffer->data, chunk_size);

        new_buffer->data += chunk_size;
        current_buffer->data += chunk_size;
        current_buffer->length -= chunk_size;

        if (current_buffer->length == 0) {
            buffer_t temp = current_buffer;
            current_buffer = current_buffer->next;
            free(temp);
        }

        n -= chunk_size;
    }

    new_buffer->data -= n;
    new_buffer->length = n;
    return new_buffer;
}
```

