import express from "express";
import sqlite3 from "sqlite3";

const app = express();
app.use(express.json());

const db = new sqlite3.Database(":memory:");

db.run(`
  CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
  )
`);

app.post("/login", (req, res) => {
  const { username, password } = req.body;

  // ❌ VULNERABLE CODE
  const query = `
    SELECT * FROM users
    WHERE username = '${username}'
    AND password = '${password}'
  `;

  db.get(query, (err, row) => {
    if (err) {
      return res.status(500).send(err.message);
    }

    if (row) {
      res.send("Logged in!");
    } else {
      res.status(401).send("Invalid credentials");
    }
  });
});

app.listen(3000, () => {
  console.log("Server running on port 3000");
});