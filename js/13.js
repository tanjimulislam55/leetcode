const romanToInteger = (roman) => {
  object = { I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000 };
  let intVal = 0;
  for (let i = 0; i < roman.length - 1; i++) {
    let currAlph = roman[i];
    let nextAlph = roman[i + 1];
    if (object[currAlph] >= object[nextAlph]) {
      intVal += object[currAlph];
    } else {
      intVal -= object[currAlph];
    }
  }
  return intVal + object[roman.substr(-1)];
};

console.log(romanToInteger("MCMXCIV")); // 1994
console.log(romanToInteger("VII")); // 7
console.log(romanToInteger("LVIII")); // 58
console.log(romanToInteger("III")); // 3
