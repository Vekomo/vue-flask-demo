<template>
  <div>
    <b-alert variant="danger" show = 3>{{ message }}</b-alert>
    <br>
  </div>
</template>

<script>
export default {
  props: ['message'],
};
</script>
