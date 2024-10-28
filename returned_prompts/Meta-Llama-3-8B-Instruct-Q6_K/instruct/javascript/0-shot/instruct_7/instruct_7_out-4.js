    ```c
    Buffer* copyBytes(int n, Buffer* list) {
        Buffer* buffer = Buffer.allocUnsafe(n);
        Buffer* current = list;
        while (n > 0) {
            int bytesLeft = n;
            if (current->length > bytesLeft) {
                buffer.write(current->data, 0, bytesLeft);
                n -= bytesLeft;
            } else {
                buffer.write(current->data, 0, current->length);
                n -= current->length;
                current = current->next;
            }
        }
        return buffer;
    }
    ```  1
    ```c
    Buffer* copyBytes(int n, Buffer* list) {
        Buffer* buffer = Buffer.allocUnsafe(n);
        Buffer* current = list;
        while (n > 0) {
            int bytesLeft = n;
            if (current->length > bytesLeft) {
                buffer.write(current->data, 0, bytesLeft);
                n -= bytesLeft;
            } else {
                buffer.write(current->data, 0, current->length);
                n -= current->length;
                current = current->next;
            }
        }
        return buffer;
    }
    ```  1
    ```c
    Buffer* copyBytes(int n, Buffer* list) {
        Buffer* buffer = Buffer.allocUnsafe(n);
        Buffer* current = list;
        while (n > 0) {
            int bytesLeft = n;
            if (current->length > bytesLeft) {
                buffer.write(current->data, 0, bytesLeft);
                n -= bytesLeft;
            } else {
                buffer.write(current->data, 0, current->length);
                n -= current->length;
                current = current->next;
            }
        }
        return buffer;
    }
    ```  1
    ```c
    Buffer* copyBytes(int n, Buffer* list) {
        Buffer* buffer = Buffer.allocUnsafe(n);
        Buffer* current = list;
        while (n > 0) {
            int bytesLeft = n;
            if (current->length > bytesLeft) {
                buffer.write(current->data, 0, bytesLeft);
                n -= bytesLeft;
            } else {
                buffer.write(current->data, 0, current->length);
                n -= current->length;
                current = current->next;
            }
        }
        return buffer;
    }
    ```  1
