<template>
    <div>
      <div>
        <b-button v-b-toggle.sidebar-1>...</b-button>
        <b-sidebar id="sidebar-1" title="Tables+" shadow>
          <div class="px-1 py-2">
            <router-link to="/tech_master">Technology Master</router-link> <br>
            <router-link to="/os_tech_master">OS Tech Master</router-link> <br>
            <router-link to="/data_tech_master">Data Tech Master</router-link> <br>
            <router-link to="/app_tech_master">App Tech Master</router-link> <br>
          </div>
        </b-sidebar>
  </div>
  <div class ="container">
    <div class = "row justify-content-md-center">
      <h1>OS Master</h1>
    </div>
    <div class = "row">
      <table class="table table-hover">
        <thead>
          <tr>
            <th scope="col">technology_name</th>
            <th scope="col">OS_technology_name</th>
            <th scope="col">OS_tech_dependant_tags</th>
            <th scope="col">OS_tech_description</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(entry, index) in response" :key="index">
            <td>{{ entry.technology_id }}</td>
            <td>{{ entry.OS_technology_name }}</td>
            <td>{{ entry.OS_tech_dependant_tags }}</td>
            <td>{{ entry.OS_tech_description }}</td>
            <td>
            </td>
            <td>
              <div class="btn-group" role="group">
                <button type="button" class="btn btn-warning btn-sm"
                          v-b-modal.os-update-modal
                          @click="editOS(entry)">
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
  <b-modal ref="addOSModal"
         id="table-modal"
         title="Add an entry to OS Master"
         hide-footer>
    <b-form @submit="onSubmit" class="w-100">
      <b-form-group id = "form-os-fk-group"
                    label = "Technology name"
                    label-for="fk-input">
        <b-form-select id ='fk-input'
                       v-model="addForm.id"
                       required
                       :options="tech">

        </b-form-select>
       </b-form-group>
      <b-form-group id="form-os-name-group"
                    label="OS_name:"
                    label-for="form-os-name-input">
          <b-form-input id="form-os-name-input"
                         type="text"
                         required
                         maxlength=50
                         v-model="addForm.name">
                       </b-form-input>
      </b-form-group>
      <b-form-group id="form-os-tags-group"
                    label="OS_tags:"
                    label-for="form-os-tags-input">
          <b-form-input id="form-os-tags-input"
                         type="text"
                         required
                         maxlength=2000
                         v-model="addForm.tags">
                       </b-form-input>
      </b-form-group>
      <b-form-group id="form-os-decription-group"
                    label="OS_description:"
                    label-for="form-os-description-input">
          <b-form-input id="form-os-description-input"
                         type="text"
                         required
                         maxlength=500
                         v-model="addForm.description">
                       </b-form-input>
      </b-form-group>
      <b-button type="submit" variant="primary">Submit</b-button>
    </b-form>
</b-modal>
<b-modal ref="editOSModal"
         id="os-update-modal"
         title="Update"
         hide-footer>
  <b-form @submit="onSubmitUpdate" class="w-100">
    <b-form-group id = "form-os-fk-edit-group"
                  label = "Technology name"
                  label-for="fk-edit-input">
      <b-form-select id ='fk-edit-input'
                     v-model="editForm.technology_id"
                     required
                     :options="tech">

      </b-form-select>
    </b-form-group>
  <b-form-group id="form-name-edit-group"
                label="OS_name:"
                label-for="form-name-edit-input">
      <b-form-input id="form-name-edit-input"
                    type="text"
                    v-model="editForm.name"
                    required
                    maxlength=50
                    placeholder="Enter name">
      </b-form-input>
    </b-form-group>
    <b-form-group id="form-os-tag-edit-group"
                  label="OS_tags:"
                  label-for="form-os-tag-edit-input">
        <b-form-input id="form-os-tag-edit-input"
                      type="text"
                      v-model="editForm.tags"
                      required
                      maxlength=2000
                      placeholder="Enter tags">
        </b-form-input>
      </b-form-group>
    <b-form-group id="form-os-description-edit-group"
                  label="OS_description:"
                  label-for="form-os-description-edit-input">
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
import PathMixins from '../mixins/pathMixins';

export default {
  mixins: [PathMixins],
  data() {
    return {
      response: [],
      tech_id: [],
      tech_map: {},
      display_map: {},
      addForm: {
        id: null,
        name: '',
        tags: '',
        description: '',
      },
      editForm: {
        technology_id: null,
        old_name: '',
        name: '',
        tags: '',
        description: '',
      },
      tech: [{ text: 'Select One', value: null }],
    };
  },
  methods: {
    getOS() {
      const path = this.get_os_path;
      axios.get(path)
        .then((res) => {
          this.response = res.data;

          for (let i = 0; i < this.response.length; i += 1) {
            this.response[i].technology_id = this.display_map[this.response[i].technology_id];
          }
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addOS(payload) {
      const path = this.add_os_path;
      axios.post(path, payload)
        .then(() => {
          this.getOS();
        })
        .catch((error) => {
          console.log(error);
          this.getOS();
        });
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addOSModal.hide();
      const payload = {
        technology_id: this.tech_map[this.addForm.id],
        OS_technology_name: this.addForm.name,
        OS_tech_dependant_tags: this.addForm.tags,
        OS_tech_description: this.addForm.description,
      };
      console.log(payload);
      this.addOS(payload);
    },
    getTechId() {
      const path = this.get_tech_path;
      axios.get(path)
        .then((res) => {
          this.tech_id = res.data;
          let i;
          for (i = 0; i < this.tech_id.length; i += 1) {
            if (!this.tech.includes(this.tech_id[i].technology_id)) {
              this.tech.push(this.tech_id[i].technology_name);
              this.tech_map[this.tech_id[i].technology_name] = this.tech_id[i].technology_id;
              this.display_map[this.tech_id[i].technology_id] = this.tech_id[i].technology_name;
            }
          }
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    editOS(entry) {
      this.editForm = entry;
      this.editForm.old_name = entry.OS_technology_name;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editOSModal.hide();
      const payload = {
        technology_id: this.tech_map[this.editForm.technology_id],
        OS_technology_name: this.editForm.old_name,
        OS_tech_dependant_tags: this.editForm.tags,
        OS_tech_description: this.editForm.description,
      };
      this.updateOS(payload, this.editForm.name);
    },
    // eslint-disable-next-line
    updateOS(payload, os_name) {

      const path = this.update_os_path + os_name; // eslint-disable-line
      axios.put(path, payload)
        .then(() => {
          this.getOS();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getOS();
        });
    },
    // eslint-disable-next-line
    removeEntry(os_name) {
      const path = this.delete_os_path + os_name; // eslint-disable-line
      axios.delete(path)
        .then(() => {
          this.getOS();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getOS();
        });
    },
    onDeleteEntry(entry) {
      this.removeEntry(entry.OS_technology_name);
    },
  },
  created() {
    this.getTechId();
    this.getOS();
    console.log('Succesful.');
  },
};
</script>
