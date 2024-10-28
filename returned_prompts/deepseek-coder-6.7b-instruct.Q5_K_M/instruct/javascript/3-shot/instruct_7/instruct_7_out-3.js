    Buffer *copyBuffer(int n, Buffer *list) {
        Buffer *newBuffer = Buffer.allocUnsafe(n);
        Buffer *current = list;
        int copied = 0;

        while (copied < n && current != NULL) {
            int toCopy = min(n - copied, current->size);
            memcpy(newBuffer->data + copied, current->data, toCopy);
            copied += toCopy;
            current = current->next;
        }

        n = copied;
        return newBuffer;
    }

