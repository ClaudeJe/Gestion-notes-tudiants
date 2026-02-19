<template>
  <div class="container mt-4">
    <h1 class="text-center mb-4">Gestion des Notes</h1>

    <nav class="mb-4">
      <router-link to="/" class="btn btn-primary me-2">Étudiants</router-link>
      <router-link to="/notes" class="btn btn-success me-2">Notes</router-link>
      <router-link to="/averages" class="btn btn-warning">Moyennes</router-link>
    </nav>

    <router-view />
  </div>
</template>
