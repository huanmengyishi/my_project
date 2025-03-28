<script setup>
import {useRouter} from 'vue-router';
import FrontView from "@/views/FrontView.vue";

const router = useRouter();
const handleClick = () => {
  router.push('/');
}
</script>
<!-- 主布局组件 -->
<!-- NewView.vue -->
<template>
  <div class="container">
    <!-- 固定头部 -->
    <FrontView class="fixed-header"/>

    <!-- 主要内容容器 -->
    <main class="main-container">
      <!-- 二级路由出口（渲染TwoNewView） -->
      <RouterView />

      <!-- 固定返回按钮 -->
      <t-button
        class="fixed-bottom"
        @click="handleClick"
      >
        返回上一页
      </t-button>
    </main>
  </div>
</template>
<style scoped>
.container {
  position: relative;
  height: 100vh;
  overflow: hidden;
}

.fixed-header {
  position: fixed;
  top: 0;
  left: 20%;
  width: 80%;
  height: 48px;
  z-index: 1000;
  background: white;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.main-container {
  margin-top: 60px;
  height: calc(100vh - 60px);
  position: relative;
}

.fixed-bottom {
  position: fixed;
  top: 0;
  left: 0;
  height: 48px;
  transform: none;
  z-index: 1001;
  background: white;
}
</style>
