<template>
  <div class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
    <div class="container">
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo03"
              aria-controls="navbarTogglerDemo03" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <a class="navbar-brand p-0" href="/">
        <img src="132.png" alt="132" width="60">
      </a>
    </div>
      <div class="collapse navbar-collapse" id="navbarTogglerDemo03">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link btn btn-link" :class="{active: $route.href === '/'}" aria-current="page"
               @click="$router.push('/')">Home</a>
          </li>
        </ul>
      <div>
    </div>
  </div>


  </div>
</template>

<script>

</script>

<style scoped>

</style>