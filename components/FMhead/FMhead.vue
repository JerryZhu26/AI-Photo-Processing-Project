<template>
	<view class="FM-head">
		<view class="FM-head-icon">
			<text class="iconfont icon-sousuo"></text>
		</view>
		{{title}}
	</view>
</template>

<script>
	export default {

		data() {
			return {
				
			};
		},
		props : ['title']
	}
</script>

<style scoped>
		.FM-head {  
			width: 100%;  
			height: 75px;  
			font-size: 16px;  
			line-height: 80px;  
			text-align: center;  
			
			position: fixed;  
			top: 0;  
			left: 0;  
			z-index: 1000;  
			background-color: white;   
		}  
		.FM-head-icon {  
			position: absolute;  
			right: 8px;  
			top: 50%;  
			transform: translateY(-50%);  
			width: 90px;  
			height: 30px;  
			color: cornflowerblue;   
			line-height: 30px;  
		} 
</style>