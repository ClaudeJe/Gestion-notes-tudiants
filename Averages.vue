<template>
  <div>
    <h2>Moyennes</h2>

    <table class="table table-striped">
      <thead>
        <tr>
          <th>Étudiant</th>
          <th>Moyenne</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(avg, name) in averages" :key="name">
          <td>{{ name }}</td>
          <td>{{ avg.toFixed(2) }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "AveragesPage",
  data() {
    return {
      averages: {}
    }
  },
  mounted() {
    axios.get('http://127.0.0.1:5000/averages')
      .then(res => this.averages = res.data)
      .catch(err => console.error(err))
  }
}
</script>
