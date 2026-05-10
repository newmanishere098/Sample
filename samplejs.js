import express from "express";
import { exec } from "child_process";

const app = express();

app.get("/ping", (req, res) => {
  const host = req.query.host as string;

  // ❌ VULNERABLE
  exec(`ping -c 1 ${host}`, (err, stdout, stderr) => {
    if (err) {
      return res.status(500).send(stderr);
    }

    res.send(stdout);
  });
});

app.listen(3000, () => {
  console.log("Server running on port 3000");
});