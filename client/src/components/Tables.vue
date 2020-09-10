<button type="button" class="btn btn-primary">{{ "Technology_Master" }}</button>
<button type="button" class="btn btn-primary">{{ "OS_Tech_Master" }}</button>
<button type="button" class="btn btn-primary">{{ "Data_Tech_Master" }}</button>
<button type="button" class="btn btn-primary">{{ "App_Tech_Master" }}</button>

<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <button v-on:click="get_tech_master" type="button" class="btn btn-primary">
            {{ "Technology_Master" }}
        </button>
        <button v-on:click="get_os_master" type="button" class="btn btn-primary">
          {{ "OS_Tech_Master" }}
        </button>
        <button v-on:click="get_data_master" type="button" class="btn btn-primary">
          {{ "Data_Tech_Master" }}
        </button>
        <button v-on:click="get_app_master" type="button" class="btn btn-primary">{{
          "App_Tech_Master" }}
        </button>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Col1</th>
              <th scope="col">Col2</th>
              <th scope="col">Col3</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(entry, index) in response" :key="index">
              <td>{{ entry }}</td>
              <td>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm">Update</button>
                  <button type="button" class="btn btn-danger btn-sm">Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        <button type="button" class="btn btn-success btn-sm">Add</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      response: [],
    };
  },
  methods: {
    get_tech_master() {
      const path = 'http://localhost:5000/get_tech_master';
      axios.get(path)
        .then((res) => {
          this.response = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    get_os_master() {
      const path = 'http://localhost:5000/get_os_master';
      axios.get(path)
        .then((res) => {
          this.response = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    get_data_master() {
      const path = 'http://localhost:5000/get_data_master';
      axios.get(path)
        .then((res) => {
          this.response = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    get_app_master() {
      const path = 'http://localhost:5000/get_app_master';
      axios.get(path)
        .then((res) => {
          this.response = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    console.log('Succesful.');
  },
};
</script>
