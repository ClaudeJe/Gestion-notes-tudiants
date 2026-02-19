import { createRouter, createWebHistory } from 'vue-router'

import LoginPage from '../components/Login.vue'
import StudentList from '../components/StudentList.vue'
import NoteList from '../components/NoteList.vue'
import AveragesPage from '../components/Averages.vue'

const routes = [
  {
    path: '/',
    redirect: '/login'
  },
  {
    path: '/login',
    component: LoginPage
  },
  {
    path: '/students',
    component: StudentList   // ✅ corrigé ici
  },
  {
    path: '/notes',
    component: NoteList
  },
  {
    path: '/averages',
    component: AveragesPage
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router