//This feels a bit brute force-ish, but it's my own work.

exports.toRoman = function(num) {
  if (num >= 4000) return; //Apparently, standard roman numerals can represent numbers up to 3,999

  //The github hint helped a lot
  //I divided algorithm into 2 parts : Lazy Roman Numerals and Modern Numerals
  //Part 1a: Lazy Numerals, simply count number of thousands, hundreds, tens, ones, and if there are fiveHundred, fifty and five
  let thousands = Math.floor(num % 10000 / 1000);
  num -= 1000 * thousands;
  
  let fiveHundreds = num >= 500 ? true : false;
  if (fiveHundreds)
    num -= 500;
  
  let hundreds = Math.floor(num % 1000 / 100);
  num -= 100 * hundreds;

  let fifty = num >= 50 ? true : false;
  if (fifty)
    num -= 50;

  let tens = Math.floor(num % 100 / 10);
  num -= 10 * tens;
  
  let five = num >= 5 ? true : false;
  if (five)
    num -= 5;

  let ones = num;
  
  //Part 1b: using the count above, build a lazy numeral (LN) string
  let result = 'M'.repeat(thousands) + 
          'D'.repeat(fiveHundreds ? 1 : 0) +
          'C'.repeat(hundreds) +
          'L'.repeat(fifty ? 1 : 0) +
          'X'.repeat(tens) +
          'V'.repeat(five ? 1 : 0) +
          'I'.repeat(ones);

  //Part 2: convert to modern numerals (MN)
  //We need to account for incorrect representation of numbers
  result = result.replace('IIII', 'IV');
  //If number has a 9 - it results in VIV - incorrect
  result = result.replace('VIV', 'IX');

  //A common pattern emerges - 4 repeating LN (AAAA) must be replaced by a middle MN with (AB)
  result = result.replace('XXXX', 'XL');
  //Next iteration is - if there was already a middle MN (B), then (BAB) has to be corrected to (AC)
  result = result.replace('LXL', 'XC');

  //Repeat for thousands
  result = result.replace('CCCC', 'CD');
  result = result.replace('DCD', 'CM');

  return result;

};
