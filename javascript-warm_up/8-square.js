#!/usr/bin/node

const x = parseInt(process.argv[2], 10);

if (Number.isNaN(x)) {
  console.log('Missing size');
} else {
    for (let i = 0; i < x; i++) {
      let line = '';
     for (let n = 0; n < x ; n++) {
        line += 'X';
    }
  console.log(line)
}
}
