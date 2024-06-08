"use strict";

const fs = require("fs");

module.exports = {
  cat: fs.readFileSync(__dirname + "/cat.hjson", "utf8"),
};
