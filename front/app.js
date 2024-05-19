const express = require('express');
const axios = require('axios');

const app = express();
const PORT = 3000;

app.get('/', (req, res) => {
  const data = {
    message: 'Hello World',
  };

  res.json(data);
});

app.get('/users/:id', async (req, res) => {
  const userId = req.params.id;

  try {
    const response = await axios.get(`http://compose-api-1:8000/users/${userId}`);

    res.send(response.data);
  } catch (error) {
    console.error('Error al obtener información del usuario:', error);

    res.status(500).send('Error al obtener información del usuario');
  }
});

app.listen(PORT, () => {
  console.log(`Servidor Express corriendo en el puerto ${PORT}`);
});
