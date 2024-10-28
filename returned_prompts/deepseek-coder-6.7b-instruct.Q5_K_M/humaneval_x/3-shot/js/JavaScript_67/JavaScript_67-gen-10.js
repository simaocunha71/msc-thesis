  let [apple_s, orange_s] = s.match(/\d+/g).map(Number);
  return n - apple_s - orange_s;
}



