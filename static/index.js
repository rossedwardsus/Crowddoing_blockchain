'use strict';

const Project = httpVueLoader('/static/project.vue')
const Sidebar = httpVueLoader('/static/sidebar.vue')
const AddProject = httpVueLoader('/static/add_project.vue')
const EditProject = httpVueLoader('/static/edit_project.vue')


// 0. If using a module system (e.g. via vue-cli), import Vue and VueRouter
// and then call `Vue.use(VueRouter)`.

// 1. Define route components.
// These can be imported from other files
const Foo = { 
		template: '<div>twitter/google trends/google news/cryptocompare</div>' 
}
const Bar = { template: '<div>bar</div>' }

// 2. Define some routes
// Each route should map to a component. The "component" can
// either be an actual component constructor created via
// `Vue.extend()`, or just a component options object.
// We'll talk about nested routes later.
const routes = [
  { path: '/project/add', component: AddProject},
  { path: '/project/edit', component: EditProject},
  { path: '/project/:projectId', name: 'project', component: Project, props: true },
  { path: '/bar', component: Bar },
  { path: '/sidebar', component: Sidebar}

]

// 3. Create the router instance and pass the `routes` option
// You can pass in additional options here, but let's
// keep it simple for now.
const router = new VueRouter({
  mode: "history", 
  routes // short for `routes: routes`
})

// 4. Create and mount the root instance.
// Make sure to inject the router with the router option to make the
// whole app router-aware.
const app = new Vue({
  router
}).$mount('#app')

// Now the app has started!


