const oddCount = (lst) => lst.map(str => str.split('').filter(x => +x % 2).length)
