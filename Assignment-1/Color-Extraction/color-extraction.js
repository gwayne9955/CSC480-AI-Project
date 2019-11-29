const { resolve } = require('path');
const ColorThief = require('colorthief');

const img = Promise.resolve(process.cwd(), '3F.jpg');

ColorThief.getColor(img)
    .then(color => { console.log(color) })
    .catch(err => { console.log(err) })

ColorThief.getPalette(img, 5)
    .then(palette => { console.log(palette) })
    .catch(err => { console.log(err) })
    
