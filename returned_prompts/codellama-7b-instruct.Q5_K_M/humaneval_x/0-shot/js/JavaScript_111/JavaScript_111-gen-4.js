const histogram = (test) => {
    let result = {};
    let arr = test.split(" ");
    let max = 0;
    for (let i = 0; i < arr.length; i++) {
        if (!result[arr[i]]) {
            result[arr[i]] = 1;
        }
        else {
            result[arr[i]]++;
            if (result[arr[i]] > max) {
                max = result[arr[i]];
            }
        }
    }
    for (let i in result) {
        if (result[i] == max) {
            return [i, max];
        }
    }
};

B:
const histogram = (test) => {
    const counts = test.split(' ').reduce((acc, curr) => {
      acc[curr] = acc[curr] ? acc[curr] + 1 : 1;
      return acc;
    }, {});

    return Object.entries(counts).reduce((acc, [key, value]) => {
      if (value === Math.max(...Object.values(counts))) {
        acc.push(key);
      }
      return acc;
    }, []);
  };

C:
const histogram = (test) => {
    const histogram = {};
    for (const letter of test) {
        if (letter in histogram) {
            histogram[letter]++;
        } else {
            histogram[letter] = 1;
        }
    }
    const max = Math.max(...Object.values(histogram));
    return Object.entries(histogram).filter(([, count]) => count === max).map(([letter]) => letter);
};

D:
const histogram = (test) => {
    const histogram = {};
    for (const letter of test) {
        histogram[letter] = histogram[letter] ? histogram[letter] + 1 : 1;
    }
    const max = Math.max(...Object.values(histogram));
    return Object.entries(histogram).filter(([, count]) => count === max).map(([