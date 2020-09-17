import Vue from 'vue';
import Router from 'vue-router';
import Home from './components/Home.vue';
import TechMasterTables from './components/TechMasterTables.vue';
import AppMasterTables from './components/AppMasterTables.vue';
import DataMasterTables from './components/DataMasterTables.vue';
import OSMasterTables from './components/OSMasterTables.vue';
import Ping from './components/Ping.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/tech_master',
      name: 'TechMasterTables',
      component: TechMasterTables,
    },
    {
      path: '/os_tech_master',
      name: 'OSMasterTables',
      component: OSMasterTables,
    },
    {
      path: '/data_tech_master',
      name: 'DataMasterTables',
      component: DataMasterTables,
    },
    {
      path: '/app_tech_master',
      name: 'AppMasterTables',
      component: AppMasterTables,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
  ],
});
