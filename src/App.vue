<script setup>
import NewFind from "@/views/Home.vue";
</script>
<template>
  <Suspense>
    <template #default>
      <NewFind v-if="toggleNewFind"/>
    </template>
    <template #fallback>
      <div>组件加载中...</div>
    </template>
  </Suspense>
  <router-view />
</template>
<style scoped>
nav {
  width: 100%;
  font-size: 1rem;
  text-align: center;
  margin-top: auto;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  nav {
    margin-top: 0;
    justify-content: flex-end;
  }
}
</style>
