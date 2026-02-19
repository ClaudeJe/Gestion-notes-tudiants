<template>
  <div>
    <h2>Notes</h2>

    <table class="table table-bordered">
      <thead>
        <tr>
          <th>Étudiant</th>
          <th>Note</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="note in notes" :key="note.id">
          <td>{{ note.student_name }}</td>
          <td>{{ note.score }}</td>
          <td>
            <button class="btn btn-danger btn-sm" @click="deleteNote(note.id)">
              Supprimer
            </button>
          </td>
        </tr>
      </tbody>
    </table>

    <h4>Ajouter une note</h4>

    <select v-model="selectedStudent" class="form-select mb-2">
      <option disabled value="">Choisir étudiant</option>
      <option v-for="student in students" :key="student.id" :value="student.id">
        {{ student.name }}
      </option>
    </select>

    <input type="number" v-model="newScore" class="form-control mb-2" placeholder="Note">

    <button class="btn btn-success" @click="addNote">
      Ajouter
    </button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      notes: [],
      students: [],
      newScore: '',
      selectedStudent: ''
    }
  },
  mounted() {
    this.loadNotes()
    this.loadStudents()
  },
  methods: {
    loadNotes() {
      axios.get('http://127.0.0.1:5000/notes')
        .then(res => this.notes = res.data)
    },
    loadStudents() {
      axios.get('http://127.0.0.1:5000/students')
        .then(res => this.students = res.data)
    },
    addNote() {
      axios.post('http://127.0.0.1:5000/notes', {
        score: this.newScore,
        student_id: this.selectedStudent
      }).then(() => {
        this.newScore = ''
        this.selectedStudent = ''
        this.loadNotes()
      })
    },
    deleteNote(id) {
      axios.delete(`http://127.0.0.1:5000/notes/${id}`)
        .then(() => this.loadNotes())
    }
  }
}
</script>
