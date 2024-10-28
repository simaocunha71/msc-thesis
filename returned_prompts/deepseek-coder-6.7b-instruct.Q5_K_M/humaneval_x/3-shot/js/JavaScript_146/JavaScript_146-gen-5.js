  return nums.filter(num => num > 10 && 
                            (Math.abs(num) % 10) % 2 === 1 && 
                            Math.floor(num / 10) % 10 % 2 === 1).length;
}



