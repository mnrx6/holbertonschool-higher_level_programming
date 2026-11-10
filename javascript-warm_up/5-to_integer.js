#!/usr/bin/node

const mynumber = process.argv[2];
const number = parseInt(mynumber, 10);

if (Number.isNaN(number)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${number}`);
}
