<template>
  <div class="col">
    <div class="card">
      <img src="132.png" class="card-img-top" alt="img">
      <div class="card-body">
        <h5 class="card-title">product</h5>
        <h5 class="card-title">product</h5>
        <p class="card-text"></p>
      </div>
      <ul class="list-group list-group-flush">
        <li class="list-group-item">Type:</li>
        <li class="list-group-item">Price:</li>
        <li class="list-group-item">Discount:</li>
      </ul>
      <div class="card-body">
        <button @click="" type="button" class="btn btn-dark" data-bs-toggle="modal"
                data-bs-target="#product">
          Edit
        </button>

        <div class="modal fade" id="product" tabindex="-1" aria-labelledby="editeModalLabel"
             aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h1 class="modal-title fs-5" id="editModalLabel">Edit</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
              </div>
              <div class="modal-footer">
                <button type="submit" class="btn btn-success" @click="">Button</button>
                <button type="button" class="btn btn-dark" data-bs-dismiss="modal">Button</button>
              </div>
            </div>
          </div>
        </div>

        <button type="button" class="btn btn-dark" data-bs-toggle="modal"
                data-bs-target="#deleteProduct" style="margin-left: 5px;">
          Delete
        </button>

        <div class="modal fade" id="deleteProduct" tabindex="-1"
             aria-labelledby="deleteModalLabel" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h1 class="modal-title fs-5" id="deleteModalLabel">Delete</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <h3>Are you sure?</h3>
              </div>
              <div class="modal-footer">
                <button @click="" type="button" class="btn btn-danger">Yes</button>
                <button type="button" class="btn btn-dark" data-bs-dismiss="modal">No</button>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>

</template>

<script>

</script>

<style>

</style>