<template>
    <div>
      <vs-button @click='activePrompt = true' color='primary' type='border'>
        New
      </vs-button>
      <vs-table :data='response'>
        <template slot='header'>
        <h3>
          Data Master
        </h3>
      </template>
      <template slot ='thead'>
        <vs-th>
          Technology Name
        </vs-th>
        <vs-th>
          Name
        </vs-th>
        <vs-th>
          Tags
        </vs-th>
        <vs-th>
          Description
        </vs-th>
        <vs-th>
          Actions
        </vs-th>
      </template>

      <template slot-scope='{data}'>
        <vs-tr :key='index' v-for='(entry, index) in data'>
          <vs-td :data='data[index].technology_id'>
            {{data[index].technology_id}}
          </vs-td>
          <vs-td :data='data[index].Data_technology_name'>
            {{data[index].Data_technology_name}}
          </vs-td>
          <vs-td :data='data[index].Data_tech_dependant_tags'>
            {{data[index].Data_tech_dependant_tags}}
          </vs-td>
          <vs-td :data='data[index].Data_tech_description'>
            {{data[index].Data_tech_description}}
          </vs-td>
          <vs-td>
            <vs-button icon='edit' size='small' @click='editData(data[index])'></vs-button>
            <vs-button icon='delete' color='danger' size='small' @click='onDeleteEntry(data[index])'></vs-button>
          </vs-td>

        </vs-tr>
      </template>
      </vs-table>
      <vs-prompt
      title='New entry'
      :active.sync='activePrompt'
      @accept='onSubmit'>
        <vs-select
          label='Technology Name'
          v-model='addForm.id'>
          <vs-select-item
          :key='index'
          :value='item'
          :text='item'
          v-for='item,index in tech' />
        </vs-select>
        <vs-input label='Name' placeholder ='Name' v-model='addForm.name'/>
        <vs-input label='Tags' placeholder ='Tags' v-model='addForm.tags'/>
        <vs-input label='Description' placeholder ='Description' v-model='addForm.description'/>
      </vs-prompt>
      <vs-prompt
      title='Edit entry'
      :active.sync='editPrompt'
      @accept='onSubmitUpdate'>
        <vs-select
          label='Technology Name'
          v-model='addForm.id'>
          <vs-select-item
          :key='index'
          :value='item'
          :text='item'
          v-for='item,index in tech' />
        </vs-select>
        <vs-input label='Name' placeholder='Name' v-model='editForm.name'/>
        <vs-input label='Tags' placeholder ='Tags' v-model='editForm.tags'/>
        <vs-input label='Description' placeholder ='Description' v-model='editForm.description'/>
      </vs-prompt>
    </div>
</template>

<script>
import axios from 'axios';
import PathMixins from '../mixins/pathMixins';

export default {
  mixins: [PathMixins],
  data() {
    return {
      activePrompt: false,
      editPrompt: false,
      response: [],
      tech_id: [],
      tech_keys: [],
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
      tech: [],
    };
  },
  methods: {
    getData() {
      const path = this.get_data_path;
      axios.get(path)
        .then((res) => {
          this.response = res.data.data;

          for (let i = 0; i < this.response.length; i += 1) {
            this.response[i].technology_id = this.display_map[this.response[i].technology_id];
          }

        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addData(payload) {
      const path = this.add_data_path;
      axios.post(path, payload)
        .then((res) => {

          this.response = res.data.data;
          console.log(res.data.message);
          for (let i = 0; i < this.response.length; i += 1) {
            this.response[i].technology_id = this.display_map[this.response[i].technology_id];
          }
        })
        .catch((error) => {
          console.log(error);
          this.getData();
        });
    },
    onSubmit() {

      const payload = {
        technology_id: this.tech_map[this.addForm.id],
        Data_technology_name: this.addForm.name,
        Data_tech_dependant_tags: this.addForm.tags,
        Data_tech_description: this.addForm.description,
      };
      this.addData(payload);
    },
    getTechId() {
      this.tech_id = JSON.parse(localStorage.getItem('tech_response'));
      let i;
      for (i = 0; i < this.tech_id.length; i += 1) {
        if (!this.tech.includes(this.tech_id[i].technology_id)) {
          this.tech.push(this.tech_id[i].technology_name);
          this.tech_map[this.tech_id[i].technology_name] = this.tech_id[i].technology_id;
          this.display_map[this.tech_id[i].technology_id] = this.tech_id[i].technology_name;
        }
      } //loop
    },
    editData(entry) {
      this.editPrompt = true;
      this.editForm = entry;
      this.editForm.old_name = entry.Data_technology_name;
    },
    onSubmitUpdate() {

      const payload = {
        technology_id: this.tech_map[this.editForm.technology_id],
        New_Data_technology_name: this.editForm.name,
        Data_technology_name: this.editForm.old_name,
        Data_tech_dependant_tags: this.editForm.tags,
        Data_tech_description: this.editForm.description,
      };
      this.updateData(payload);
    },
    // eslint-disable-next-line
    updateData(payload, data_name) {

      const path = this.update_data_path; // eslint-disable-line
      axios.put(path, payload)
        .then((res) => {
          this.response = res.data.data;

          for (let i = 0; i < this.response.length; i += 1) {
            this.response[i].technology_id = this.display_map[this.response[i].technology_id];
          }
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getData();
        });
    },
    // eslint-disable-next-line
    removeEntry(data_name_delete) {
      const path = this.delete_data_path; // eslint-disable-line
      const payload = { data_name: data_name_delete };
      axios.put(path, payload)
        .then((res) => {
          this.response = res.data.data;

          for (let i = 0; i < this.response.length; i += 1) {
            this.response[i].technology_id = this.display_map[this.response[i].technology_id];
          }
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
    this.getTechId();
    this.getData();
    console.log('Succesful.');
  },
};
</script>
