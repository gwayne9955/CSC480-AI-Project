const { resolve } = require('path');
const ColorThief = require('colorthief');

var myArgs = process.argv.slice(2);

const img = resolve(process.cwd(), myArgs[0]);

ColorThief.getColor(img)
    .then(color => {
      console.log("The primary color has RBG " + color);
      var red = color[0];
      var green = color[1];
      var blue = color[2];
      if (red > 105 && green < 80) {
         console.log("The strawberry is ripe");
      }
      else {
         console.log("The strawberry is not ripe");
      }
   })
    .catch(err => { console.log(err) })

// ColorThief.getPalette(img, 5)
//     .then(palette => { console.log(palette) })
//     .catch(err => { console.log(err) })
