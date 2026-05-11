// vulnerable.js
const express = require("express");
const app = express();

app.get("/", (req, res) => {
    const name = req.query.name;

    // VULNERABLE: Reflected XSS
    res.send(`<h1>Hello ${name}</h1>`);
});

app.listen(3000, () => {
    console.log("Server running");
});