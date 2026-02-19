import axios from 'axios';

const API_URL = 'http://localhost:5000';

export function getStudents() {
    return axios.get(`${API_URL}/students`);
}

export function addStudent(name) {
    return axios.post(`${API_URL}/students`, { name });
}

export function deleteStudent(id) {
    return axios.delete(`${API_URL}/students/${id}`);
}

export function getNotes() {
    return axios.get(`${API_URL}/notes`);
}

export function addNote(score, student_id) {
    return axios.post(`${API_URL}/notes`, { score, student_id });
}

export function deleteNote(id) {
    return axios.delete(`${API_URL}/notes/${id}`);
}

export function getAverages() {
    return axios.get(`${API_URL}/averages`);
}
