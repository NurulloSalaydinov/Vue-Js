<template>
    <div class="block" v-if="showBlock" @click="stopTimer">
        Click Me !
    </div>    
</template>

<script>
export default {
    props: ['delay'],
    data() {
        return {
            showBlock: false,
            timer: null,
            reactionTime: 0
        }
    },
    mounted() {
        setTimeout(() => {
            this.showBlock = true
            this.startTimer()
        }, this.delay)
    },
    methods: {
        startTimer() {
            this.timer = setInterval(() => {
                this.reactionTime += 10
            }, 10)
        },
        stopTimer() {
            clearInterval(this.timer)
            this.$emit('end', this.reactionTime)
        }
    }
}
</script>

<style>

    .block {
        width: 400px;
        font-size: 30px;
        padding: 60px 0;
        cursor: pointer;
        color: #fff;
        margin: 40px auto;
        text-align: center;
        border-radius: 20px;
        background: #1eff00;
    }

</style>
