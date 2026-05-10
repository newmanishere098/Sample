import express from "express";

const app = express();

app.get("/user", (req, res) => {
  const username = req.query.username;

  // ❌ Vulnerable
  const query =
    `SELECT * FROM users WHERE username = '${username}'`;

  res.send(query);
});

app.listen(3000);