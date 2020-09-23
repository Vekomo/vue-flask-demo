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
    <alert :message ='message' v-if='showMessage'></alert>
    <div class = "row justify-content-md-center">
      <h1>Technology Master</h1>
    </div>
    <div class = "row">
      <table class="table table-hover">
        <thead>
          <tr>
            <th scope="col">technology_id</th>
            <th scope="col">Tech_name</th>
            <th scope="col">tech_dependant_tags</th>
            <th scope="col">stack_description</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(entry, index) in response" :key="index">
            <td>{{ entry.technology_id }}</td>
            <td>{{ entry.technology_name }}</td>
            <td>{{ entry.tech_dependant_tags }}</td>
            <td>{{ entry.stack_description }}</td>
            <td>
            </td>
            <td>
              <div class="btn-group" role="group">
                <button type="button" class="btn btn-warning btn-sm"
                          v-b-modal.tech-update-modal
                          @click="editTech(entry)">
                          Update
                </button>
                <button type="button" class="btn btn-danger btn-sm"
                          @click="onDeleteEntry(entry)">Delete</button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
      <button type="button" class="btn btn-success btn-sm" v-b-modal.table-modal>Add</button>
    </div>
  </div>
  <b-modal ref="addTechModal"
         id="table-modal"
         title="Add an entry to Tech Master"
         hide-footer>
    <b-form @submit="onSubmit" class="w-100">
      <b-form-group id="form-tech-name-group"
                    label="Tech_name:"
                    label-for="form-tech-name-input">
          <b-form-input id="form-tech-name-input"
                         type="text"
                         required
                         maxlength=50
                         v-model="addForm.name">
                       </b-form-input>
      </b-form-group>
      <b-form-group id="form-tech-tags-group"
                    label="Tech_tags:"
                    label-for="form-tech-tags-input">
          <b-form-input id="form-tech-tags-input"
                         type="text"
                         required
                         maxlength=2000
                         v-model="addForm.tags">
                       </b-form-input>
      </b-form-group>
      <b-form-group id="form-stack-decription-group"
                    label="stack_description:"
                    label-for="form-stack_description-input">
          <b-form-input id="form-stack-description-input"
                         type="text"
                         required
                         maxlength=500
                         v-model="addForm.description">
                       </b-form-input>
      </b-form-group>
      <b-button type="submit" variant="primary">Submit</b-button>
    </b-form>
</b-modal>
<b-modal ref="editTechModal"
         id="tech-update-modal"
         title="Update"
         hide-footer>
  <b-form @submit="onSubmitUpdate" class="w-100">
  <b-form-group id="form-name-edit-group"
                label="Tech_name:"
                label-for="form-name-edit-input">
      <b-form-input id="form-name-edit-input"
                    type="text"
                    v-model="editForm.name"
                    required
                    maxlength=50
                    placeholder="Enter name">
      </b-form-input>
    </b-form-group>
    <b-form-group id="form-tech-tag-edit-group"
                  label="Tech_tags:"
                  label-for="form-tech-tag-edit-input">
        <b-form-input id="form-tech-tag-edit-input"
                      type="text"
                      v-model="editForm.tags"
                      required
                      maxlength=2000
                      placeholder="Enter tags">
        </b-form-input>
      </b-form-group>
    <b-form-group id="form-tech-description-edit-group"
                  label="Tech_description"
                  label-for="form-tech-description-edit-input">
      <b-form-input id="form-tech-description-edit-input"
                    type="text"
                    v-model="editForm.description"
                    required
                    maxlength=500
                    placeholder="Enter description">
      </b-form-input>
    </b-form-group>
    <b-button-group>
      <b-button type="submit" variant="primary">Update</b-button>
      <b-button type="reset" variant="danger">Cancel</b-button>
    </b-button-group>
  </b-form>
</b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  data() {
    return {
      response: [],
      addForm: {
        name: '',
        tags: '',
        description: '',
      },
      editForm: {
        technology_id: null,
        name: '',
        tags: '',
        description: '',
      },
      message: 'Cannot delete entry, belongs to child table.',
      showMessage: false,
    };
  },
  methods: {
    getTech() {
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
    addTech(payload) {
      const path = 'http://127.0.0.1:5000/add_tech';
      axios.post(path, payload)
        .then(() => {
          this.getTech();
        })
        .catch((error) => {
          console.log(error);
          this.getTech();
        });
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addTechModal.hide();
      const payload = {
        technology_name: this.addForm.name,
        tech_dependant_tags: this.addForm.tags,
        stack_description: this.addForm.description,
      };
      console.log(payload);
      this.addTech(payload);
    },
    editTech(entry) {
      this.editForm = entry;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editTechModal.hide();
      const payload = {
        technology_name: this.editForm.name,
        tech_dependant_tags: this.editForm.tags,
        stack_description: this.editForm.description,
      };
      this.updateTech(payload, this.editForm.technology_id);
    },
    // eslint-disable-next-line
    updateTech(payload, tech_id) {

      const path = 'http://localhost:5000/update_tech/' + tech_id; // eslint-disable-line
      axios.put(path, payload)
        .then(() => {
          this.getTech();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getTech();
        });
    },
    // eslint-disable-next-line
    removeEntry(tech_id) {
      const path = 'http://localhost:5000/delete_tech/' + tech_id; // eslint-disable-line
      axios.delete(path)
        .then((response) => {
          if (response.data.status) {
            this.showMessage = true;
          } else {
            this.showMessage = false;
          }
          console.log(response.data.status);
          this.getTech();
        })
        .catch((error) => {
          console.error(error);
          console.log('Bing bong bing there was a pwoblem');
          this.getTech();
        });
    },
    onDeleteEntry(entry) {
      this.removeEntry(entry.technology_id);
    },
  },
  created() {
    this.getTech();
    console.log('Succesful.');
  },
  components: {
    alert: Alert,
  },
};
</script>
