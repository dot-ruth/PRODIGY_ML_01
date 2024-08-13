<template>
  <div id="app">
    <div class="container">
      <h1>House Price Prediction</h1>
      <form @submit.prevent="predictPrice">
        <div>
          <label for="squareFootage">Square Footage:</label>
          <input type="number" v-model="squareFootage" placeholder="Enter square footage" required />
        </div>
        <div>
          <label for="bedrooms">Number of Bedrooms:</label>
          <input type="number" v-model="bedrooms" placeholder="Enter number of bedrooms" required />
        </div>
        <div>
          <label for="bathrooms">Number of Bathrooms:</label>
          <input type="number" v-model="bathrooms" placeholder="Enter number of bathrooms" required />
        </div>
        <button type="submit">Predict Price</button>
      </form>
      <div v-if="price !== null" class="result">
        <h2>Predicted House Price: ${{ price.toFixed(2) }}</h2>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  data() {
    return {
      squareFootage: '',
      bedrooms: '',
      bathrooms: '',
      price: null
    };
  },
  methods: {
    async predictPrice() {
      try {
        const response = await axios.post('http://127.0.0.1:5000/predict', {
          GrLivArea: parseFloat(this.squareFootage),
          BedroomAbvGr: parseFloat(this.bedrooms),
          FullBath: parseFloat(this.bathrooms)
        });
        this.price = response.data.price;
      } catch (error) {
        console.error('Error making prediction:', error);
      }
    }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.container {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  max-width: 500px;
  margin: 0 auto;
}

h1 {
  margin-bottom: 20px;
}

form div {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

.result {
  margin-top: 20px;
  font-size: 1.5em;
}
</style>
