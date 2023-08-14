<template>
  <section class="app" style="margin-top: 10vh;">
    <div class="container my-5">
      <product-list></product-list>
    </div>
  </section>
</template>

<script>
// @ is an alias to /src
import ProductList from "@/components/ProductList.vue";
export default {
  components: {
    ProductList
  },
}
</script>
