
    ```js
    function copy(n, list) {
      const buffer = Buffer.allocUnsafe(n);
      while (n) {
        const chunk = list.first;
        const size = Math.min(n, chunk.length);
        chunk.copy(buffer, buffer.length - n, 0, size);
        n -= size;
        if (!(list = list.next)) break;
      }
      return buffer;
    }
    ```

    1. The function should be named `copy`.
    2. The function should take two arguments: `n`, the number of bytes to copy, and `list`, a pointer to the head of the list of buffered data chunks.
    3. The function should allocate a new buffer of the appropriate size using `Buffer.allocUnsafe()`.
    4. The function should copy the data from the list of chunks to the new buffer, updating the `n` variable to reflect the number of bytes copied.
    5. The function should return the newly allocated buffer.
    6. The function should be designed to be inlinable.
    7. The function should not use any application-specific variables or libraries.

- Write a function in C that copies a specified number of bytes from a list of buffered data chunks and returns the resulting buffer. The function should be designed to be inlinable and should not use any application-specific variables or libraries. The function should take two arguments: `n`, the number of bytes to copy, and `list`, a pointer to the head of the list of buffered data chunks. The function should allocate a new buffer of the appropriate size using `Buffer.allocUnsafe()` and then copy the data from the list of chunks to the new buffer, updating the `n` variable to reflect the number of bytes copied. The function should return the newly allocated buffer.

    ```js
    function copy(n, list) {
      const buffer = Buffer.allocUnsafe(n);
      while (n) {
        const chunk = list.first;
        const size = Math.min(n, chunk.length);
        chunk.copy(buffer, buffer.length - n, 0, size);
        n -= size;
        if (!(list = list.next)) break