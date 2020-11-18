<template>
    <div>
      <vs-button @click='activePrompt = true' color='primary' type='border'>
        New
      </vs-button>
      <vs-table :data='response'>
        <template slot='header'>
        <h3>
          Tech Master
        </h3>
      </template>
      <template slot ='thead'>
        <vs-th>
          Id
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
          <vs-td :data='data[index].technology_name'>
            {{data[index].technology_name}}
          </vs-td>
          <vs-td :data='data[index].tech_dependant_tags'>
            {{data[index].technology_name}}
          </vs-td>
          <vs-td :data='data[index].stack_description'>
            {{data[index].stack_description}}
          </vs-td>
          <vs-td>
            <vs-button icon='edit' size='small' @click='editTech(data[index])'></vs-button>
            <vs-button icon='delete' color='danger' size='small' @click='onDeleteEntry(data[index])'></vs-button>
          </vs-td>

        </vs-tr>
      </template>
      </vs-table>
      <vs-prompt
      title='New entry'
      :active.sync='activePrompt'
      @accept='onSubmit'>
        <vs-input label='Name' placeholder ='Name' v-model='addForm.name'/>
        <vs-input label='Tags' placeholder ='Tags' v-model='addForm.tags'/>
        <vs-input label='Description' placeholder ='Description' v-model='addForm.description'/>
      </vs-prompt>
      <vs-prompt
      title='Edit entry'
      :active.sync='editPrompt'
      @accept='onSubmitUpdate'>
        <vs-input label='Name' v-model='editForm.name'/>
        <vs-input label='Tags' v-model='editForm.tags'/>
        <vs-input label='Description' v-model='editForm.description'/>
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
      nameError: false,
      tagError: false,
      descriptionError: false,
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
      message: 'Cannot delete entry, technology name used in child table.',
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
    addTech(payload) {
      const path = this.add_tech_path;
      axios.post(path, payload)
        .then((res) => {
          this.response = res.data.data;
        })
        .catch((error) => {
          console.log(error);
          this.getTech();
        });
    },
    onSubmit() {

      if (this.addForm.name.length > 50) {
        this.nameError = true;
        // eslint-disable-next-line
      } else if (this.addForm.name.length < 1) {
        this.nameError = true;
      } else {
        this.nameError = false;
      }
      if (this.addForm.tags.length < 1) {
        this.tagError = true;
        // eslint-disable-next-line
      } else {
        this.tagError = false;
      }
      if (this.addForm.description.length < 1) {
        this.descriptionError = true;
        // eslint-disable-next-line
      } else {
        this.descriptionError = false;
      }

      if (this.descriptionError == true || this.nameError == true || this.tagError == true) {
        return;
      }

      const payload = {
        technology_name: this.addForm.name,
        tech_dependant_tags: this.addForm.tags,
        stack_description: this.addForm.description,
      };
      console.log(payload);
      this.addTech(payload);
    },
    editTech(entry) {
      this.editPrompt = true;
      //this.editForm = entry;
      this.editForm = Object.assign({}, entry);
    },
    onSubmitUpdate() {
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
          this.response = res.data.data;
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
          if (response.data.status === 500) {
            this.$vs.notify({title:'Cannot delete entry',text:'This entries technology name used in child table.',color:'danger'})
          } else {
            this.response = response.data.data;
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
