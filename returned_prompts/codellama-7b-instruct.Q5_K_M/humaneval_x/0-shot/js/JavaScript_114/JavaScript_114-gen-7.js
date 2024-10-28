  const minSubArraySum = nums => {
    let minSum = 0;
    for (let i = 0; i < nums.length; i++) {
      minSum += nums[i];
      for (let j = i + 1; j < nums.length; j++) {
        minSum += nums[j];
        break;
      }
    }
    return minSum;
  }

B:
  const minSubArraySum = nums => {
    let minSum = 0;
    let sum = 0;
    for (let i = 0; i < nums.length; i++) {
      sum += nums[i];
      minSum = Math.min(minSum, sum);
    }
    return minSum;
  }

C:
  const minSubArraySum = nums => {
    let minSum = 0;
    for (let i = 0; i < nums.length; i++) {
      let sum = 0;
      for (let j = i; j < nums.length; j++) {
        sum += nums[j];
        minSum = Math.min(minSum, sum);
      }
    }
    return minSum;
  }

D:
  const minSubArraySum = nums => {
    let minSum = 0;
    for (let i = 0; i < nums.length; i++) {
      let sum = 0;
      for (let j = i; j < nums.length; j++) {
        sum += nums[j];
        minSum = Math.min(minSum, sum);
      }
    }
    return minSum;
  }

E:
  const minSubArraySum = nums => {
    let minSum = 0;
    for (let i = 0; i < nums.length; i++) {
      let sum = 0;
      for (let j = i; j < nums.length; j++) {
        sum += nums[j];
        minSum = Math.min(minSum, sum);
      }
    }
   