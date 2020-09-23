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
      <h1>Data Master</h1>
    </div>
    <div class = "row">
      <table class="table table-hover">
        <thead>
          <tr>
            <th scope="col">technology_name</th>
            <th scope="col">Data_technology_name</th>
            <th scope="col">Data_tech_dependant_tags</th>
            <th scope="col">Data_tech_description</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(entry, index) in response" :key="index">
            <td>{{ entry.technology_id }}</td>
            <td>{{ entry.Data_technology_name }}</td>
            <td>{{ entry.Data_tech_dependant_tags }}</td>
            <td>{{ entry.Data_tech_description }}</td>
            <td>
            </td>
            <td>
              <div class="btn-group" role="group">
                <button type="button" class="btn btn-warning btn-sm"
                          v-b-modal.data-update-modal
                          @click="editData(entry)">
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
  <b-modal ref="addDataModal"
         id="table-modal"
         title="Add an entry to Data Master"
         hide-footer>
    <b-form @submit="onSubmit" class="w-100">
      <b-form-group id = "form-data-fk-group"
                    label = "Technology name"
                    label-for="fk-input">
        <b-form-select id ='fk-input'
                       v-model="addForm.id"
                       required
                       :options="tech">

        </b-form-select>
       </b-form-group>
      <b-form-group id="form-data-name-group"
                    label="Data_name:"
                    label-for="form-data-name-input">
          <b-form-input id="form-data-name-input"
                         type="text"
                         required
                         maxlength=50
                         v-model="addForm.name">
                       </b-form-input>
      </b-form-group>
      <b-form-group id="form-data-tags-group"
                    label="Data_tags:"
                    label-for="form-data-tags-input">
          <b-form-input id="form-data-tags-input"
                         type="text"
                         required
                         maxlength=2000
                         v-model="addForm.tags">
                       </b-form-input>
      </b-form-group>
      <b-form-group id="form-data-decription-group"
                    label="Data_description:"
                    label-for="form-data-description-input">
          <b-form-input id="form-data-description-input"
                         type="text"
                         required
                         maxlength=500
                         v-model="addForm.description">
                       </b-form-input>
      </b-form-group>
      <b-button type="submit" variant="primary">Submit</b-button>
    </b-form>
</b-modal>
<b-modal ref="editDataModal"
         id="data-update-modal"
         title="Update"
         hide-footer>
  <b-form @submit="onSubmitUpdate" class="w-100">
    <b-form-group id = "form-data-fk-edit-group"
                  label = "Technology name"
                  label-for="fk-edit-input">
      <b-form-select id ='fk-edit-input'
                     v-model="editForm.technology_id"
                     required
                     :options="tech">

      </b-form-select>
    </b-form-group>
  <b-form-group id="form-name-edit-group"
                label="Data_name:"
                label-for="form-name-edit-input">
      <b-form-input id="form-name-edit-input"
                    type="text"
                    v-model="editForm.name"
                    required
                    maxlength=50
                    placeholder="Enter name">
      </b-form-input>
    </b-form-group>
    <b-form-group id="form-data-tag-edit-group"
                  label="Data_tags:"
                  label-for="form-data-tag-edit-input">
        <b-form-input id="form-data-tag-edit-input"
                      type="text"
                      v-model="editForm.tags"
                      required
                      maxlength=2000
                      placeholder="Enter tags">
        </b-form-input>
      </b-form-group>
    <b-form-group id="form-data-description-edit-group"
                  label="Data_description:"
                  label-for="form-data-description-edit-input">
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
    getData() {
      const path = this.get_data_path;
      axios.get(path)
        .then((res) => {
          this.response = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addData(payload) {
      const path = this.add_data_path;
      axios.post(path, payload)
        .then(() => {
          this.getData();
        })
        .catch((error) => {
          console.log(error);
          this.getData();
        });
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addDataModal.hide();
      const payload = {
        technology_id: this.tech_map[this.addForm.id],
        Data_technology_name: this.addForm.name,
        Data_tech_dependant_tags: this.addForm.tags,
        Data_tech_description: this.addForm.description,
      };
      console.log(payload);
      this.addData(payload);
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
    editData(entry) {
      this.editForm = entry;
      this.editForm.old_name = entry.Data_technology_name;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editDataModal.hide();
      const payload = {
        technology_id: this.tech_map[this.editForm.technology_id],
        New_Data_technology_name: this.editForm.name,
        Data_technology_name: this.editForm.old_name,
        Data_tech_dependant_tags: this.editForm.tags,
        Data_tech_description: this.editForm.description,
      };
      this.updateData(payload, this.editForm.name);
    },
    // eslint-disable-next-line
    updateData(payload, data_name) {

      const path = this.update_data_path + data_name; // eslint-disable-line
      axios.put(path, payload)
        .then(() => {
          this.getData();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getData();
        });
    },
    // eslint-disable-next-line
    removeEntry(data_name) {
      const path = this.delete_data_path + data_name; // eslint-disable-line
      axios.delete(path)
        .then(() => {
          this.getData();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getData();
        });
    },
    onDeleteEntry(entry) {
      this.removeEntry(entry.Data_technology_name);
    },
  },
  created() {
    this.getData();
    this.getTechId();
    console.log('Succesful.');
  },
};
</script>
