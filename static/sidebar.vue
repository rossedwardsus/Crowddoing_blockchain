<template>
      <div>
      	<li v-for="item in projects">
      		<h3>1sidebar1</h3>
      	</li>
      </div>
</template>

<script>

	module.exports = {
	  name: 'sidebar',
	  data(){ return {projects: ["one", "two"]}}
	}

</script>

<style>
	
	.hello {
	    background-color: #ffe;
	}

</style>
