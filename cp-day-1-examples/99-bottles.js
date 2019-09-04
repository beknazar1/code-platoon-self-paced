function bottles(num) {
  if (num < 1) {
    console.log('No more bottles of beer on the wall, no more bottles of beer.');
    console.log('Go to the store and buy some more, 99 bottles of beer on the wall.');
    return;
  }
  console.log(`${howMany(num)} of beer on the wall, ${howMany(num)} of beer.`);
  num--;
  console.log(`Take one down and pass it around, ${howMany(num)} of beer on the wall.`);
  bottles(num);
}

function howMany(num) {
  if (num > 1) 
    return `${num} bottles`;
  else if (num === 1)
    return '1 bottle';
  else 
    return 'no more bottles';
}

bottles(99);