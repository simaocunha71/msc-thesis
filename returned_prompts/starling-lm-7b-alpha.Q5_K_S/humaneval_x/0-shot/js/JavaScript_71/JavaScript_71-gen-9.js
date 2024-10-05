let maxLen = 0;
let tempLen = 0;
for (let i = 0; i < str.length; i++) {
  if (i === 0 || str[i] !== str[i - 1]) tempLen = 1;
  else tempLen++;
  maxLen = Math.max(maxLen, tempLen);
}
return maxLen;
};

/*
