    Buffer* copyBytes(int n, Buffer* list) {
        Buffer* buffer = Buffer.allocUnsafe(n);
        Buffer* current = list;
        while (n > 0) {
            Buffer* chunk = current;
            int chunkSize = chunk->size;
            if (chunkSize > n) {
                memcpy(buffer->data, chunk->data, n);
                buffer->size = n;
                break;
            }
            memcpy(buffer->data, chunk->data, chunkSize);
            buffer->size += chunkSize;
            n -= chunkSize;
            current = current->next;
        }
        return buffer;
    }