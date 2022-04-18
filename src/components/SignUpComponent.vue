<template>
  <div class="col-5 mx-auto card p-5 bg-dark text-light">
    <form method="POST">
      <div class="row">
        <div class="col-6">
          <label class="form-label">Имя</label>
          <input v-model="name" type="text" class="form-control">
        </div>
        <div class="col-6">
          <label class="form-label">Фамилия</label>
          <input v-model="surname" type="text" class="form-control">
        </div>
      </div>
      <div class="mb-3">
        <label class="form-label">E-mail</label>
        <input v-model="email" type="email" class="form-control">
      </div>
      <div class="mb-3">
        <label class="form-label">Пароль</label>
        <input v-model="password" type="password" class="form-control">
      </div>
      <button v-on:click="send" type="button" class="btn btn-primary">Зарегистрироваться</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'SignUpComponent',

  data () {
    return {
      response: null
    }
  },
  methods: {
    send () {
      axios
        .post('http://127.0.0.1:5000/api/v1/signup',
          {
            headers: {
              'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': '*',
              'Access-Control-Allow-Headers': 'Origin, Content-Type, X-Auth-Token, Authorization, Accept,charset,boundary,Content-Length'
            },
            data: {
              name: this.name,
              surname: this.surname,
              email: this.email,
              token: '12345',
              password: this.password,
              created_at: '18.04.2022'
            }
          }
        )
        .then(response => {
          console.log(response.data)
        })
        .catch(function (error) {
          alert(error)
        })
    }
  }
}
</script>
