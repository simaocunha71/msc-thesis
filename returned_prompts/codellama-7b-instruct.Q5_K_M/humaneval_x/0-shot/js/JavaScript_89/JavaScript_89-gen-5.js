const encrypt = (s) => s.split('').map(c => String.fromCharCode(c.charCodeAt(0) + 2 * 2)).join('');

