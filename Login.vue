<template>
  <div class="login-container">
    <div class="login-box">
      <h2>Connexion</h2>

      <form @submit.prevent="login">
        <div class="form-group">
          <label>Email</label>
          <input 
            type="text" 
            v-model="email" 
            placeholder="Entrez votre email"
            required
          />
        </div>

        <div class="form-group">
          <label>Mot de passe</label>
          <input 
            type="password" 
            v-model="password" 
            placeholder="Entrez votre mot de passe"
            required
          />
        </div>

        <button type="submit">Se connecter</button>

        <p v-if="error" class="error">{{ error }}</p>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoginPage",

  data() {
    return {
      email: "",
      password: "",
      error: ""
    }
  },

  methods: {
    login() {
      // Identifiants de test
      const validEmail = "admin"
      const validPassword = "admin123"

      if (this.email === validEmail && this.password === validPassword) {
        // Stocker un faux token
        localStorage.setItem("token", "fake-jwt-token")

        // Redirection vers students
        this.$router.push("/students")
      } else {
        this.error = "Email ou mot de passe incorrect"
      }
    }
  }
}
</script>

<style scoped>
.login-container {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f4f6f9;
}

.login-box {
  width: 350px;
  padding: 30px;
  background: white;
  border-radius: 8px;
  box-shadow: 0 5px 15px rgba(0,0,0,0.1);
}

h2 {
  text-align: center;
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 15px;
}

input {
  width: 100%;
  padding: 8px;
  border-radius: 5px;
  border: 1px solid #ccc;
}

button {
  width: 100%;
  padding: 10px;
  background-color: #42b983;
  border: none;
  color: white;
  font-weight: bold;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #369f6b;
}

.error {
  margin-top: 10px;
  color: red;
  text-align: center;
}
</style>
