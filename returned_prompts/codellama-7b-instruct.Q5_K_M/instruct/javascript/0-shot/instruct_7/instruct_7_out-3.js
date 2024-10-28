
    function copyBuffer(n, list) {
        const buf = Buffer.allocUnsafe(n);
        let total = 0;
        while (n > 0 && list) {
            const chunk = list.chunk;
            const nb = Math.min(chunk.length, n);
            buf.set(chunk.slice(0, nb), total);
            total += nb;
            n -= nb;
            list = list.next;
        }
        return buf;
    }

