var rn = require("./romanNumerals");

console.log(rn.toRoman(1) === 'I' ? 'PASS' : `1 Expected I, but got ${rn.toRoman(1)}`);
console.log(rn.toRoman(3) === 'III' ? 'PASS' : `3 Expected III, but got ${rn.toRoman(3)}`);
console.log(rn.toRoman(4) === 'IV' ? 'PASS' : `4 Expected IV, but got ${rn.toRoman(4)}`);
console.log(rn.toRoman(9) === 'IX' ? 'PASS' : `9 Expected IX, but got ${rn.toRoman(9)}`);
console.log(rn.toRoman(14) === 'XIV' ? 'PASS' : `14 Expected XIV, but got ${rn.toRoman(14)}`);
console.log(rn.toRoman(44) === 'XLIV' ? 'PASS' : `44 Expected XLIV, but got ${rn.toRoman(44)}`);
console.log(rn.toRoman(944) === 'CMXLIV' ? 'PASS' : `944 Expected CMXLIV, but got ${rn.toRoman(944)}`);
console.log(rn.toRoman(1357) === 'MCCCLVII');
console.log(rn.toRoman(99) === "XCIX");
console.log(rn.toRoman(500) === "D");
console.log(rn.toRoman(3999) === "MMMCMXCIX");