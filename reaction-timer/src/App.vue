<template>
<div>
  <h1>Vue Reaction Timer</h1>
  <button class="play-btn" :disabled="isPlaying" @click="Start">Play</button>
  <Block v-if="isPlaying" :delay="delay" @end="endGame" />
  <Results v-if="score" :result="score" />
</div>
</template>

<script>
import Block from '@/components/Block.vue';
import Results from './components/Results.vue';

export default {
  name: 'App',
  components: {
    Block,
    Results
},
  data() {
    return {
      isPlaying: false,
      delay: null,
      score: null
    }
  },
  methods: {
    Start() {
      this.delay = 2000 + Math.random() * 5000
      this.isPlaying = true
      this.score = null
    },
    endGame(reactionTime) {
      this.score = reactionTime
      this.isPlaying = false
    }
  }
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #444;
  margin-top: 60px;
}
.play-btn {
  outline: none;
  cursor: pointer;
  font-size: 20px;
  color: #fff;
  border-radius: 10px;
  padding: 12px 100px;
  font-weight: medium;
  transition: all 0.3s;
  background: #1eff00;
  border: 1px solid #1eff00;
}
.play-btn:hover {
  color: #1eff00;
  background: transparent;
}
.play-btn[disabled] {
  opacity: 0.5;
  cursor: not-allowed
}
.play-btn[disabled]:hover {
  color: #fff;
  background: #1eff00;
}
</style>
