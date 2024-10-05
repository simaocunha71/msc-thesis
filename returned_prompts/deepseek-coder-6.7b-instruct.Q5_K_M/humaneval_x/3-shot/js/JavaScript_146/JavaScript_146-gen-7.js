  return nums.filter(num => num > 10 && [...num.toString().slice(0,1), ...num.toString().slice(-1)].every(n => '13579'.includes(n))).length;
}



