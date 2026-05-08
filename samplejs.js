const express = require('express');
const mysql = require('mysql2/promise');
const fs = require('fs/promises');
const path = require('path');
const { spawn } = require('child_process');

const app = express();
app.use(express.json());

// Environment-based credentials
const dbConfig = {
    host: process.env.DB_HOST,
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    database: process.env.DB_NAME
};

const VALID_USERNAME = /^[a-zA-Z0-9_]{3,20}$/;

app.post('/login', async (req, res) => {

    try {

        const username = req.body.username;
        const password = req.body.password;

        // Input validation
        if (!VALID_USERNAME.test(username)) {
            return res.status(400).send('Invalid username format');
        }

        const connection = await mysql.createConnection(dbConfig);

        // Parameterized query
        const [rows] = await connection.execute(
            'SELECT id FROM users WHERE username = ? AND password = ?',
});
