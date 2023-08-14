<template>
    <div class="container my-5" style="min-height: 70vh;">
        <div class="row row-cols-1 row-cols-md-2 row-cols-lg-5  g-5">
            <product-card>

            </product-card>
        </div>
    </div>
</template>

<script>
import ProductCard from '@/components/ProductCard.vue';

export default {
    components: {
        ProductCard
    },
    props: {
        employees: {
            type: Array,
            required: true
        },
    },
    name: 'product-list'

}
</script>

<style>

</style>