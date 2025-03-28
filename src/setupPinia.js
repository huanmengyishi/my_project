// src/setupPinia.js
import { createApp } from 'vue';
import { createPinia, setActivePinia } from 'pinia';

// 创建 Vue 应用实例
const app = createApp({});
const pinia = createPinia();

// 初始化 Pinia
app.use(pinia);
setActivePinia(pinia);

export { pinia };