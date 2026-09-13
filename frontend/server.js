const express = require('express');
const cors = require('cors');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;
const FASTAPI_URL = process.env.FASTAPI_URL || 'http://127.0.0.1:8000';

app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

// Proxy endpoint for chat to FastAPI backend
app.post('/api/chat', async (req, res) => {
    try {
        const response = await fetch(`${FASTAPI_URL}/api/chat`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(req.body),
        });

        const data = await response.json();
        if (!response.ok) {
            return res.status(response.status).json(data);
        }
        res.json(data);
    } catch (err) {
        console.error('Error proxying to FastAPI:', err.message);
        res.status(500).json({ detail: 'Failed to communicate with Python FastAPI backend. Ensure FastAPI server is running on port 8000.' });
    }
});

app.get('/health', (req, res) => {
    res.json({ status: 'ok', server: 'Node.js Express Frontend', backend: FASTAPI_URL });
});

app.listen(PORT, () => {
    console.log(`🚀 Express Web Server running at http://localhost:${PORT}`);
    console.log(`🔗 Proxying API requests to FastAPI at ${FASTAPI_URL}`);
});
