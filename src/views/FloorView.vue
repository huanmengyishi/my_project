<!-- FloorView.vue (替代原来的多个*View.vue) -->
<template>
  <div class="floor-view-container">
    <h2>{{ floorLabel }}详情</h2>

    <!-- 动态内容区域 -->
    <div class="dynamic-content">
      <router-view v-slot="{ Component }">
        <keep-alive :max="5">
          <component
            :is="Component"
            :key="$route.meta.cacheKey"
          />
        </keep-alive>
      </router-view>
    </div>

    <!-- 共享操作栏 -->
    <div class="fixed-action-bar">
      <t-button @click="$router.push('/newworld')">返回</t-button>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()

// 楼层标签映射
const floorLabel = computed(() => {
  const map: Record<string, string> = {
    one: '一楼',
    two: '二楼',
    three: '三楼',
    four: '四楼',
    five: '五楼'
  }
  return map[route.params.floor as string] || '未知楼层'
})
</script>