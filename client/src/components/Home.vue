<template>
    <div>
      <div>
        <b-button v-b-toggle.sidebar-1>...</b-button>
        <b-sidebar id="sidebar-1" title="Tables+" shadow>
          <div class="px-3 py-2">
            <router-link to="/tech_master">Technology Master</router-link> <br>
            <router-link to="/os_tech_master">OS Tech Master</router-link> <br>
            <router-link to="/data_tech_master">Data Tech Master</router-link> <br>
            <router-link to="/app_tech_master">App Tech Master</router-link> <br>
          </div>
        </b-sidebar>
  </div>
    <div class ="container">
      <div class = "row justify-content-md-center">
        <router-link to="/tech_master">Technology Master</router-link>
        <router-link to="/os_tech_master">OS Tech Master</router-link>
        <router-link to="/data_tech_master">Data Tech Master</router-link>
        <router-link to="/app_tech_master">App Tech Master</router-link>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      response: [],
    };
  },
  methods: {

  },
  created() {
    console.log('Succesful.');
  },
};
</script>
