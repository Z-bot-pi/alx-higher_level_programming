#!/usr/bin/node
//a class Rectangle that defines a rectangle
//use the class notation for defining your class
//The constructor must take 2 arguments: w and h,
//an instance method called rotate() that exchanges the width and the height of the rectangle
//an instance method called double() that multiples the width and the height of the rectangle by 2

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
  }

  print () {
    for (let i = 0; i < this.height; i++) console.log('X'.repeat(this.width));
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    [this.width, this.height] = [this.width * 2, this.height * 2];
  }
};
