<template>
  <div class="flex relative rounded-lg shadow-lg overflow-hidden bg-gray-800">
    <div class="w-full h-full flex-1" v-if="props.imgUrl">
      <img class="h-full w-full object-contain" :src="props.imgUrl" />
    </div>
    <div
      v-else-if="!props.lat || !props.lon || props.forceShowImgNa"
      class="w-full h-full flex-1 flex flex-col items-center justify-center pb-6"
    >
      <img src="/image-slash.svg" class="w-14" />
      <div class="text-xl font-bold text-gray-600 w-fit h-fit mt-5">
        著作権の関係で画像が表示できません
      </div>
    </div>
    <div class="w-full h-full flex-1 relative" v-if="props.lat && props.lon">
      <iframe
        :class="{
          'h-[166%] w-[166%] scale-[60%] origin-top-left': props.size == 's',
          'h-[125%] w-[125%] scale-[80%] origin-top-left': props.size == 'm',
          'h-full w-full': props.size == 'l',
        }"
        :src="`http://maps.google.co.jp/maps?&output=embed&q=loc:${props.lat},${props.lon}&z=${props.zoom}`"
        loading="lazy"
      ></iframe>
    </div>
    <div
      class="absolute bottom-2 inset-x-0 max-w-full mx-2 px-4 py-1 bg-gray-700 rounded-lg text-center shadow-md"
      v-if="props.name"
    >
      <div class="text-xs text-gray-300">{{ props.yomigana }}</div>
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
    lat: number | null;
    lon: number | null;
    zoom: number | null;
    imgUrl: string;
    name: string;
    yomigana: string;
    size: "s" | "m" | "l";
    forceShowImgNa: boolean;
  }>(),
  {
    imgUrl: "",
    lat: undefined,
    lon: undefined,
    zoom: 15,
    name: "",
    yomigana: "",
    size: "l",
    forceShowImgNa: false,
  }
);
</script>
