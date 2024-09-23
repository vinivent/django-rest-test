import axios from 'axios';

export const login = async (username_or_email, password) => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/users/login/', {
      username_or_email,
      password,
    });
    return response.data;  // Retorna os dados da resposta
  } catch (error) {
    throw error.response?.data || error.message;  // Lança o erro para ser tratado no componente
  }
};
