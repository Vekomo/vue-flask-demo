import Vue from 'vue';
import Router from 'vue-router';
import Tables from './components/Tables.vue';
import Ping from './components/Ping.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Tables',
      component: Tables,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
  ],
});
