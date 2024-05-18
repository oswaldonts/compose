const express = require('express');
const axios = require('axios');

const app = express();
const PORT = 3000;

// Endpoint para obtener información del usuario
app.get('/', async (req, res) => {
  try {
    // Realizar solicitud GET al endpoint /users/1
    const response = await axios.get('http://localhost:8000/users/1'); // Cambia la URL según la dirección de tu servidor de backend

    // Enviar la respuesta del servidor de backend como respuesta a la solicitud del cliente
    res.send(response.data);
  } catch (error) {
    console.error('Error al obtener información del usuario:', error);
    res.status(500).send('Error al obtener información del usuario');
  }
});

// Iniciar el servidor
app.listen(PORT, () => {
  console.log(`Servidor Express corriendo en el puerto ${PORT}`);
});
