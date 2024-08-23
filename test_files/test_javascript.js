const express = require('express');
const app = express();

app.get('/vulnerable', (req, res) => {
    // Cross-Site Scripting (XSS) vulnerability
    res.send(`<h1>${req.query.userInput}</h1>`);
});

app.listen(3000);
