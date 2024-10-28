const isHappy = (s) => {
    if (s.length < 3) return false;
    let temp = s.split('');
    for (let i = 0; i < temp.length - 2; i++) {
        if (temp[i] === temp[i + 1] && temp[i + 1] === temp[i + 2]) return false;
    }
    return true;
}
