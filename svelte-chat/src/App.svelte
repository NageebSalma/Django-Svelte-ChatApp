<script>
	import {onMount} from 'svelte'
	import Pusher from 'pusher-js'

	let username = 'username'
	let message = ''
	let messages = []

	onMount (() => {
	 Pusher.logToConsole = true;

     var pusher = new Pusher('50a34d118d0cc1910964', {
       cluster: 'eu'
     });

     var channel = pusher.subscribe('chat');
     channel.bind('message', function(data) {
       messages = [...messages , data]
     });
	 })

	const submit = async() => {
		await fetch('http://localhost:8000/api/messages' , {
			method : 'POST',
			headers : {'Content-Type' : 'application/json'},
			body : JSON.stringify({
				username , 
				message
			})
		})

		message = ''
	}
</script>

<div class='container'>
	<div class="d-flex flex-column align-items-stretch flex-shrink-0 bg-white" style="width: 380px;">
		<div class="d-flex align-items-center flex-shrink-0 p-3 link-dark text-decoration-none border-bottom">
		  
		  <input bind:value={username} />

		</div>
		<div class="list-group list-group-flush border-bottom scrollarea">
		{#each messages as msg}
	
		  <div class="list-group-item list-group-item-action py-3 lh-tight">
			<div class="d-flex w-100 align-items-center justify-content-between">
			  <strong class="mb-1">{msg.username}</strong>
			  <small class="text-muted">Tues</small>
			</div>
			<div class="col-10 mb-1 small">{msg.message}</div>
		  </div>
		{/each}
		</div>
</div>

<form on:submit|preventDefault = {submit}>
	<input class="form-control" placeholder="write a message" bind:value={message} />	
</form>
</div>

<style>
	.container{
		display: flex;
		justify-content: center;
		flex-direction: column;
		
	}

	.scrollarea{
		max-height: 500px;
	}
</style>
