<template>
	<vs-row vs-justify="center">
  <vs-col type="flex" vs-justify="center" vs-align="center" vs-w="3">
    <vs-card>
      <div slot="header">
        <h3>
          Technology Master tables
        </h3>
      </div>
      <div>
        <span>Click to go to Tech Tables.</span>
      </div>
			<div slot="footer">
        <vs-row vs-justify="flex-end">
          <vs-button type="gradient" color="danger" to="/techTables">TECH</vs-button>
        </vs-row>
      </div>
    </vs-card>
	 </vs-col>
	 <vs-col type="flex" vs-justify="center" vs-align="center" vs-w="3">
		<vs-card>
      <div slot="header">
        <h3>
          Data Master tables
        </h3>
      </div>
      <div>
        <span>Click to go to Data Tables.</span>
      </div>
			<div slot="footer">
        <vs-row vs-justify="flex-end">
          <vs-button type="gradient" color="danger" to="/dataTables">DATA</vs-button>
        </vs-row>
      </div>
    </vs-card>
	</vs-col>
	<vs-col type="flex" vs-justify="center" vs-align="center" vs-w="3">
		<vs-card>
      <div slot="header">
        <h3>
          App Master tables
        </h3>
      </div>
      <div>
        <span>Click to go to App Tables.</span>
      </div>
			<div slot="footer">
        <vs-row vs-justify="flex-end">
          <vs-button type="gradient" color="danger" to="/appTables">APP</vs-button>
        </vs-row>
      </div>
    </vs-card>
	</vs-col>
	<vs-col type="flex" vs-justify="center" vs-align="center" vs-w="3">
		<vs-card>
      <div slot="header">
        <h3>
          OS Master tables
        </h3>
      </div>
      <div>
        <span>Click to go to OS Tables.</span>
      </div>
			<div slot="footer">
        <vs-row vs-justify="flex-end">
          <vs-button type="gradient" color="danger" to="/osTables">OS</vs-button>
        </vs-row>
      </div>
    </vs-card>
	</vs-col>
</vs-row>
</template>

<script>
import axios from 'axios';
import PathMixins from '../mixins/pathMixins';
export default {
  mixins: [PathMixins],
  data() {
    return {
      response: [],
    };
  },
  methods: {
    getTech() {
      const path = this.get_tech_path;
      axios.get(path)
        .then((res) => {
          this.response = res.data.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getTech();
  },
  watch: {
    response: {
      handler() {
        localStorage.setItem('tech_response', JSON.stringify(this.response));
      },
    },
  },
};
</script>
