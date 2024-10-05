const antiShuffle = (s) => s.split(' ').map(w => [...w].sort((a,b) => a.charCodeAt(0) - b.charCodeAt(0)).join('')).join(' ');
