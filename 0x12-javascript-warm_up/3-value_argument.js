#!/usr/bin/node

//printing 1st argument passed to it

if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
