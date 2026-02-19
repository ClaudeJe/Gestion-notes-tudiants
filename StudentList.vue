<template>
  <div>
    <h2>Étudiants</h2>
    <ul>
      <li v-for="student in students" :key="student.id">
        {{ student.name }}
        <button @click="remove(student.id)">Supprimer</button>
      </li>
    </ul>
    <input v-model="newStudent" placeholder="Nom de l'étudiant">
    <button @click="add">Ajouter</button>
  </div>
</template>

<script>
import { getStudents, addStudent, deleteStudent } from '../services/api.js';

export default {
  data() {
    return {
      students: [],
      newStudent: ''
    }
  },
  created() {
    this.loadStudents();
  },
  methods: {
    loadStudents() {
      getStudents().then(res => { this.students = res.data });
    },
    add() {
      addStudent(this.newStudent).then(() => {
        this.loadStudents();
        this.newStudent = '';
      });
    },
    remove(id) {
      deleteStudent(id).then(() => this.loadStudents());
    }
  }
}
</script>
