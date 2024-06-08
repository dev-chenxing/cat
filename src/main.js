"use strict";

const hjson = require("hjson");

const asciiArt = require("./asciiArt");

const catLines = hjson.parse(asciiArt.cat);

for (const catLine of catLines) {
  console.log(catLine);
}
