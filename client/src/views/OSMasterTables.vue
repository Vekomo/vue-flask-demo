<template>
    <div>
      <vs-button @click='activePrompt = true' color='primary' type='border'>
        New
      </vs-button>
      <vs-table :data='response'>
        <template slot='header'>
        <h3>
          OS Master
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
          <vs-td :data='data[index].OS_technology_name'>
            {{data[index].OS_technology_name}}
          </vs-td>
          <vs-td :data='data[index].OS_tech_dependant_tags'>
            {{data[index].OS_tech_dependant_tags}}
          </vs-td>
          <vs-td :data='data[index].OS_tech_description'>
            {{data[index].OS_tech_description}}
          </vs-td>
          <vs-td>
            <vs-button icon='edit' size='small' @click='editOS(data[index])'></vs-button>
            <vs-button icon='delete' color='danger' size='small' @click='onDeleteEntry(data[index])'></vs-button>
          </vs-td>

        </vs-tr>
      </template>
      </vs-table>
      <vs-prompt
      title='New entry'
      :active.sync='activePrompt'
      :is-valid='validAddPrompt'
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
        <vs-input label='Name' placeholder ='Name' v-model='addForm.name'
        :success='nameSucc' success-text='Valid name.'
        :danger='!nameSucc' danger-text='Name must be nonempty and be no more than 50 characters.'/>
        <vs-input label='Tags' placeholder ='Tags' v-model='addForm.tags'
        :success='tagSucc' success-text='Valid tag.'
        :danger='!tagSucc' danger-text='Tags must begin with a "#".'/>
        <vs-input label='Description' placeholder ='Description' v-model='addForm.description'
        :success='descriptionSucc' success-text='Valid description.'
        :danger='!descriptionSucc' danger-text='Description must be nonempty and be no more than 500 characters.'/>
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
      tagSucc: false,
      descriptionSucc: false,
      idSucc: false,
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
      tech: [],
    };
  },
  computed:{
    validAddPrompt(){
      if(this.addForm.id != null) {
        this.idSucc = true;
      } else {
        this.idSucc = false;
      }
      if(this.addForm.name.length > 0 && this.addForm.name.length < 50) {
        this.nameSucc = true;
      } else {
        this.nameSucc = false;
      }
      if(this.isValidTag(this.addForm.tags) && this.addForm.tags.length < 2000) {
        this.tagSucc = true;
      } else {
        this.tagSucc = false;
      }
      if(this.addForm.description.length > 0 && this.addForm.description.length < 500) {
        this.descriptionSucc = true;
      } else {
        this.descriptionSucc = false;
      }
      if(this.descriptionSucc && this.nameSucc && this.tagSucc && this.idSucc) {
        return true;
      } else {
        return false;
      }
    }, //eofunction
  },
  methods: {
    isValidTag(tag) {
      let re = new RegExp('(([\#])([A-z])+(\,)*)+');
      if (tag === '') {
        return false;
      }
      return re.test(tag);
    },
    getOS() {
      const path = this.get_os_path;
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
    addOS(payload) {
      const path = this.add_os_path;
      axios.post(path, payload)
        .then((res) => {
          this.response = res.data.data;
          console.log(res.data.technology_id);
          for (let i = 0; i < this.response.length; i += 1) {
            this.response[i].technology_id = this.display_map[this.response[i].technology_id];
          }
        })
        .catch((error) => {
          console.log(error);
          this.getOS();
        });
    },
    onSubmit() {

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
      this.tech_id = JSON.parse(localStorage.getItem('tech_response'));
      let i;
      for (i = 0; i < this.tech_id.length; i += 1) {
        if (!this.tech.includes(this.tech_id[i].technology_id)) {
          this.tech.push(this.tech_id[i].technology_name);
          this.tech_map[this.tech_id[i].technology_name] = this.tech_id[i].technology_id;
          this.display_map[this.tech_id[i].technology_id] = this.tech_id[i].technology_name;
        }
      }
    },
    editOS(entry) {
      this.editPrompt = true;
      this.editForm = entry;
      this.editForm.old_name = entry.OS_technology_name;
    },
    onSubmitUpdate() {

      const payload = {
        technology_id: this.tech_map[this.editForm.technology_id],
        OS_technology_name: this.editForm.old_name,
        OS_tech_dependant_tags: this.editForm.tags,
        OS_tech_description: this.editForm.description,
        New_OS_name: this.editForm.name,
      };
      this.updateOS(payload);
    },
    // eslint-disable-next-line
    updateOS(payload, os_name) {

      const path = this.update_os_path; // eslint-disable-line
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
          this.getOS();
        });
    },
    // eslint-disable-next-line
    removeEntry(os_name_delete) {
      const path = this.delete_os_path; // eslint-disable-line
      const payload = { os_name: os_name_delete };
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
