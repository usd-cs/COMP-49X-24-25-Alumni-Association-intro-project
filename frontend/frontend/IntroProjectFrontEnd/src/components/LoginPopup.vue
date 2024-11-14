<template>
  <div v-if="show" class="login-popup-overlay">
    <div class="login-popup">
      <h2>Login</h2>
      <form @submit.prevent="handleLogin">
        <label for="username">Username</label>
        <input type="text" v-model="username" id="username" required />

        <label for="password">Password</label>
        <input type="password" v-model="password" id="password" required />

        <button type="submit">Login</button>
        <button type="button" @click="closePopup">Close</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    show: Boolean // Receive the prop to control visibility
  },
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    handleLogin() {
      console.log("Login attempted with:", this.username, this.password);
      // Emit an event to send login data back to parent
      this.$emit('login', { username: this.username, password: this.password });
    },
    closePopup() {
      this.$emit('close'); // Emit close event to hide the popup
    }
  }
};
</script>

<style>
.login-popup-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
}
.login-popup {
  background: white;
  padding: 20px;
  border-radius: 5px;
  width: 300px;
}
</style>
