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
                    <p v-if='nameError == 0'>
                      <b> Name error: Max length 50 characters.</b>
                    </p>
                    <p v-if='nameError == 1'>
                      <b> Name error: Name required.</b>
                    </p>
          <b-form-input id="form-tech-name-input"
                         type="text"
                         v-model="addForm.name">
                       </b-form-input>
      </b-form-group>
      <b-form-group id="form-tech-tags-group"
                    label="Tech_tags:"
                    label-for="form-tech-tags-input">
                    <p v-if='tagError == 0'>
                      <b> Tag error: Tag required.</b>
                    </p>
          <b-form-input id="form-tech-tags-input"
                         type="text"
                         maxlength=2000
                         v-model="addForm.tags">
                       </b-form-input>
      </b-form-group>
      <b-form-group id="form-stack-decription-group"
                    label="stack_description:"
                    label-for="form-stack_description-input">
                    <p v-if='descriptionError == 0'>
                      <b> Description error: Description required.</b>
                    </p>
          <b-form-input id="form-stack-description-input"
                         type="text"
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
                    value="What"
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
import PathMixins from '../mixins/pathMixins';

export default {
  mixins: [PathMixins],
  data() {
    return {
      nameError: -1,
      tagError: -1,
      descriptionError: -1,
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
      const path = this.get_tech_path;
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
      const path = this.add_tech_path;
      axios.post(path, payload)
        .then((res) => {
          this.response = res.data;
        })
        .catch((error) => {
          console.log(error);
          this.getTech();
        });
    },
    onSubmit(evt) {
      evt.preventDefault();

      if (this.addForm.name.length > 50) {
        this.nameError = 0;
        // eslint-disable-next-line
      } else if (this.addForm.name.length < 1) {
        this.nameError = 1;
      } else {
        this.nameError = -1;
      }
      if (this.addForm.tags.length < 1) {
        this.tagError = 0;
        // eslint-disable-next-line
      } else {
        this.tagError = -1;
      }
      if (this.addForm.description.length < 1) {
        this.descriptionError = 0;
        // eslint-disable-next-line
      } else {
        this.descriptionError = -1;
      }

      if (this.descriptionError > -1 || this.nameError > -1 || this.tagError > -1) {
        return;
      }

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
        technology_id: this.editForm.technology_id,
        technology_name: this.editForm.name,
        tech_dependant_tags: this.editForm.tags,
        stack_description: this.editForm.description,
      };
      this.updateTech(payload);
    },
    // eslint-disable-next-line
    updateTech(payload, tech_id) {

      const path = this.update_tech_path; // eslint-disable-line
      axios.put(path, payload)
        .then((res) => {
          this.response = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          // call again if fail? why?
          this.getTech();
        });
    },
    // eslint-disable-next-line
    removeEntry(tech_id) {
      const path = this.delete_tech_path; // eslint-disable-line
      const payload = { technology_id: tech_id };
      axios.put(path, payload)
        .then((response) => {
          if (response.data.status === 'fail') {
            this.showMessage = true;
          } else {
            this.showMessage = false;
            this.response = response.data;
          }
        })
        .catch((error) => {
          console.error(error);
          // call again if fail? why?
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
