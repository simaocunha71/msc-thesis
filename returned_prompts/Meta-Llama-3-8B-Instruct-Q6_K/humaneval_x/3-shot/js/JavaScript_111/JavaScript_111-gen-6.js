  if (test.length == 0) return {};
  let result = {};
  let max_count = 0;
  let max_letters = [];

  for (let letter of test.split(' ')) {
    if (result[letter]) {
      result[letter]++;
    } else {
      result[letter] = 1;
    }
    if (result[letter] > max_count) {
      max_count = result[letter];
      max_letters = [letter];
    } else if (result[letter] == max_count) {
      max_letters.push(letter);
    }
  }
  return max_count > 1 ? { [max_letters[0]]: max_count } : result;
}  // or return { [max_letters[0]]: max_count } if you want to return one entry if there's a tie
}  // or return { ...Object.keys(result).reduce((acc, letter) => (acc[letter] = result[letter], acc), {}) } for a more concise way to return the whole dictionary if there's a tie
}  // or return { ...Object.fromEntries(Object.entries(result).filter(([key, value]) => value == max_count)) } for a more concise way to return the whole dictionary if there's a tie
}  // or return (Object.keys(result).reduce((acc, letter) => (result[letter] > max_count ? (acc = { [letter]: result[letter] }, max_count = result[letter]) : acc, {})) for a more concise way to return the whole dictionary if there's a tie
}  // or return (Object.fromEntries(Object.entries(result).filter(([key, value]) => value == Math.max(...Object.values(result))))) for a more concise way to return the whole dictionary if there's a tie
}  // or return (Object.fromEntries(Object.entries(result).filter(([key, value]) => value == Math.max(...Object.keys(result).map(k => result[k]))))) for a more concise way to return the whole dictionary if there's a tie
}  // or return (Object.fromEntries(Object.entries(result).filter(([key, value]) => value == Object.values(result).reduce((acc, val) => Math.max(acc, val), 0)))) for a more concise way to return the whole dictionary if there's a tie
}  // or return (Object.fromEntries(Object.entries(result).filter(([key, value]) => value == Object.keys(result).reduce