const ColorThief = require('colorthief');

const img = resolve(process.cwd(), 'rainbow.png');

ColorThief.getColor(img)
    .then(color => {
      console.log(color);
      var red = color[0];
      var green = color[1];
      var blue = color[2];
      if (red > 105 && green < 70) {
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
