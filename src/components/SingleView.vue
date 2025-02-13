<template>
  <div
    class="flex flex-col h-full w-full rounded-lg shadow-lg overflow-hidden bg-black"
  >
    <div class="flex flex-1 w-full min-h-0">
      <div class="w-full h-full flex-1 flex flex-col" v-if="props.imgUrl">
        <img
          class="h-full w-full object-contain flex-1 min-h-0"
          :src="props.imgUrl"
        />
        <div class="ml-auto text-gray-300 text-[0.6rem] px-4 py-1">
          情報提供: JTBパブリッシング
          <span v-if="credit">/ 写真提供: {{ credit }}</span>
        </div>
      </div>
      <div
        v-else-if="!props.q || props.forceShowImgNa"
        class="w-full h-full flex-1 flex flex-col items-center justify-center pb-6"
      >
        <img src="/image-slash.svg" class="w-14" />
        <div class="text-xl font-bold text-gray-600 w-fit h-fit mt-5">
          著作権の関係で画像が表示できません
        </div>
      </div>
      <div class="w-full h-full flex-1 relative" v-if="props.q">
        <iframe
          :class="{
            'h-[166%] w-[166%] scale-[60%] origin-top-left': props.size == 's',
            'h-[125%] w-[125%] scale-[80%] origin-top-left': props.size == 'm',
            'h-full w-full': props.size == 'l',
          }"
          :src="`https://maps.google.com/maps?output=embed&q=${props.q}&z=${props.z}&hl=ja`"
          loading="lazy"
        ></iframe>
      </div>
    </div>
    <div
      class="max-w-full px-4 py-1 bg-gray-700 text-center shadow-md"
      v-if="props.name"
    >
      <div class="text-xs text-gray-300" v-if="props.yomigana">
        {{ props.yomigana }}
      </div>
      <div
        class="font-bold text-white"
        :class="{
          'text-sm': props.size == 's' || props.size == 'm',
          'text-xl': props.size == 'l',
        }"
      >
        {{ props.name }}
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const props = withDefaults(
  defineProps<{
    q?: string;
    z?: string;
    imgUrl?: string;
    name: string;
    yomigana?: string;
    size: "s" | "m" | "l";
    forceShowImgNa: boolean;
    credit?: string;
  }>(),
  {
    imgUrl: "",
    q: "",
    z: "15",
    name: "",
    size: "l",
    forceShowImgNa: false,
    credit: "",
  }
);
</script>
