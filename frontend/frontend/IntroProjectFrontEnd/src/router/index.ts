import { createRouter, createWebHistory } from 'vue-router';
import App from '../App.vue';
import LoginPopup from '../components/LoginPopup.vue';

const routes = [
  {
    path: '/',
    name: 'home',
    component: App, // This renders App.vue as the homepage
  },
  {
    path: '/login',
    name: 'login',
    component: LoginPopup, // Renders LoginPopup as a separate page (optional)
  }
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;
