<template>
    <div>
        <p class="score">Reaction time: {{ result }} ms</p>
        <p class="rank">{{ rank }}</p>
    </div>
</template>

<script>
export default {
    props: ['result'],
    data() {
        return {
            rank: null
        }
    },
    mounted() {
        if (this.result < 250) {
            this.rank = 'Ninja Fingers'
        } else if (this.result  < 400) {
            this.rank = 'Rapid Reflexes'
        } else {
            this.rank = 'Snail pace...'
        }
    }
}
</script>

<style>
    .score {
        font-size: 1em;
        font-weight: bold
    }
    .rank {
        font-size: 1.4em;
        color: #1eff00;
        font-weight: bold
    }

</style>
