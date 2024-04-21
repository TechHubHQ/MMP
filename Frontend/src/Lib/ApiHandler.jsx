import axios from 'axios';

const api_handler = axios.create({
    baseURL: 'http://localhost:8000'
});

export default api_handler;