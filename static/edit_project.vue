<template>
      <div>
      	name-token-linkedin-whitepaper-twitter-telegram-ethereum-active-cryptocoompare for token
      	<br/>
      	white paper
      	<br/>
      	token<input type="text" v-model="token">
      	<br/>
      	url<input type="text" v-model="url">
      	<br/>
      	<button v-on:click="btnClick">Add</button>
      </div>
</template>

<script>

	module.exports = {
	  name: 'sidebar',
	  data(){ 
	  	return {
	  		token: '',
	  		url: ''
	  	}
	  },
	  methods: {
	  	btnClick: function(){
	  		//alert(this.token);
	  		axios.post('http://localhost:8080/api/project/add', 
			    JSON.stringify({token: "this.token"}), // the data to post
			    { headers: {
			      'Content-type': 'application/json',
			      }
			    }).then(response => "");
	  	}
	  }
	  //,
	  //mounted () {
	  //  axios
	  //    .get('https://api.coindesk.com/v1/bpi/currentprice.json')
	  //    .then(response => (alert(JSON.stringify(response))))
	  //}
	}

</script>

<style>
	
	.hello {
	    background-color: #ffe;
	}

</style>
