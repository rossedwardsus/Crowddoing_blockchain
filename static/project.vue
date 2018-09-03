<template>
      <div>
      <h3>{{ $route.params.projectId }}({{projectId}})twitter/google trends/google news/cryptocompare</h3>
      <div><sidebar></sidebar></div>
      <div v-if="userData">
        <p>This route makes use of some option data that was passed in:</p>
        <p>{{userData.name}}({{userData.age}} yrs old)</p>
      </div>
      <ul class="nav nav-tabs" id="myTab" role="tablist">
		  <li class="nav-item">
		    <a class="nav-link active" id="home-tab" data-toggle="tab" href="#twitter" role="tab" aria-controls="Twitter" aria-selected="true">Twitter</a>
		  </li>
		  <li class="nav-item">
		    <a class="nav-link" id="profile-tab" data-toggle="tab" href="#google_trends" role="tab" aria-controls="google_trends" aria-selected="false">Google Trends</a>
		  </li>
		  <li class="nav-item">
		    <a class="nav-link" id="contact-tab" data-toggle="tab" href="#crypto_compare" role="tab" aria-controls="crypto_compare" aria-selected="false">Crypto Compare</a>
		  </li>
	  </ul>
		<div class="tab-content" id="myTabContent">
		  <div class="tab-pane fade show active" id="twitter" role="tabpanel" aria-labelledby="home-tab">twitter</div>
		  <div class="tab-pane fade" id="crypto_compare" role="tabpanel" aria-labelledby="profile-tab">crypto compare
		  	<br/>
		  	ethereum and social media aggegation volumes by time frames
		  </div>
		  <div class="tab-pane fade" id="google_trends" role="tabpanel" aria-labelledby="contact-tab">google trends-just list dates and numbers</div>
		</div>
    </div>
</template>

<script>

	//const sidebar = httpVueLoader('./sidebar.vue')

	//alert(sidebar);

	module.exports = {
	  name: "homepage",
	  props: ['projectId', 'userData'],
	  methods: {},
	  components : {
	    'sidebar': httpVueLoader('/static/sidebar.vue')
	    //sidebar: {template: '<li>This is a list item</li>'}
	  }
	}

</script>

<style>
	
	.hello {
	    background-color: #ffe;
	}

</style>
