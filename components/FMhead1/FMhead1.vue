<template>
	<view class="FM-head1">
		<view class="FM-head1-icon">
			<text class="iconfont icon-guanbi" @tap="handleToIndex"></text> | <text class="iconfont icon-fenlei"></text>
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
		methods :{
			handleToIndex(){
				uni.navigateTo({
					url:'/pages/index/index'
				})
			}
		},
		props : ['title']
	}
</script>

<style scoped>
		.FM-head1 {  
			width: 100%;  
			height: 75px;  
			font-size: 16px;  
			line-height: 80px;  
			text-align: center;  
			
			position: fixed;  
			top: 0;  
			left: 0;  
			z-index: 1000;  
			
		}  
		.FM-head1-icon {  
			position: absolute;  
			left: 8px;
			top: 26px;
			width: 90px;
			height: 31px;
			background: rgba(0,0,0,0.4);
			color: white;
			line-height: 31px;
			border-radius: 15px;
			display: flex;
			justify-content: space-evenly;
		} 
</style>