<template>
  <div id="app">
    <header>
      <h1>Welcome to My Vue App</h1>
      <button @click="showLoginPopup = true">Login</button>
    </header>
    
    <!-- Main page content -->
    <main>
      <p>This is the main page content.</p>
    </main>

    <!-- Pass the `showLoginPopup` prop to LoginPopup -->
    <LoginPopup :show="showLoginPopup" @close="showLoginPopup = false" />
  </div>
</template>

<script>
import LoginPopup from './components/LoginPopup.vue';

export default {
  components: {
    LoginPopup
  },
  data() {
    return {
      showLoginPopup: false // Controls display of login popup
    };
  }
};
</script>

<style>
/* Styles for the main page */
#app {
  font-family: Arial, sans-serif;
  text-align: center;
}
</style>
