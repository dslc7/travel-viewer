<template>
  <div
    class="fixed h-full w-full px-4 py-4 flex items-center justify-center bg-gray-900"
  >
    <div
      class="p-8 flex flex-col items-center justify-center bg-gray-800 rounded-lg"
      v-if="webSocketState == 'CLOSED'"
    >
      <div class="text-2xl font-extrabold text-gray-200">Travel Viewer</div>
      <input
        type="text"
        v-model="webSocketUrl"
        class="mt-8 px-4 py-2 rounded-md outline-none w-96 bg-gray-700 text-white"
        placeholder="WebSocket URL"
      />
      <button
        class="mt-4 w-full h-full py-2 rounded-md text-white font-bold bg-emerald-600 hover:bg-emerald-500"
        @click="connectWebSocket"
      >
        CONNECT
      </button>
    </div>
    <div
      class="h-full w-full flex flex-col items-center justify-center"
      v-else-if="webSocketState == 'CONNECTING'"
    >
      <div class="font-extrabold text-4xl text-gray-700">Travel Viewer</div>
      <div class="mt-5 text-gray-700 text-lg">Waiting for connection...</div>
    </div>
    <div
      class="h-full w-full flex flex-col items-center justify-center"
      v-else-if="views.length == 0"
    >
      <div class="font-extrabold text-4xl text-gray-700">Travel Viewer</div>
    </div>
    <div
      class="flex flex-wrap gap-4 h-full w-full items-center justify-center"
      v-else
    >
      <SingleView
        :class="{
          'h-full w-full': views.length == 1,
          'h-[49%] w-full': views.length == 2 && forceShowImgNa,
          'h-2/3 w-[48%]': views.length == 2 && !forceShowImgNa,
          'h-[49%] w-[48%]': views.length == 3 || views.length == 4,
        }"
        v-for="view of views"
        :key="`${view.imgUrl}${view.lon}${view.lat}`"
        :lat="view.lat"
        :lon="view.lon"
        :zoom="view.zoom"
        :yomigana="view.yomigana"
        :name="view.name"
        :imgUrl="view.imgUrl"
        :size="size"
        :forceShowImgNa="forceShowImgNa"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from "vue";
import SingleView from "./components/SingleView.vue";

const views = ref<View[]>([]);

const forceShowImgNa = computed(() => {
  for (let view of views.value) {
    if (view.imgUrl && view.lon && view.lat) return true;
  }
  return false;
});

const size = computed(() => {
  if (views.value.length == 1) return "l";
  else if (views.value.length == 2) return "m";
  else return "s";
});

const webSocketUrl = ref("ws://localhost:9999");
const webSocketState = ref<"CLOSED" | "CONNECTING" | "OPEN">("CLOSED");

let socket: WebSocket | undefined = undefined;

const connectWebSocket = () => {
  if (!webSocketUrl.value) return;

  const reconnect = () => {
    webSocketState.value = "CONNECTING";
    connectWebSocket();
  };

  socket = new WebSocket(webSocketUrl.value);
  socket.onopen = () => (webSocketState.value = "OPEN");
  socket.onclose = () => {
    views.value = [];
    setTimeout(reconnect, 1000);
  };
  socket.onerror = () => {};
  socket.onmessage = (ev: MessageEvent<string>) => {
    const data: View[] = JSON.parse(ev.data);
    views.value = data
      .filter((d) => {
        return d.imgUrl || (d.lat && d.lon) || d.name;
      })
      .slice(0, 5);
    console.log(views.value);
  };
};
</script>
