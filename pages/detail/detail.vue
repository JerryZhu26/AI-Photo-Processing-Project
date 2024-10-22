<template>  
  <view class="detail">  
    <FMhead1 title="播客"></FMhead1>
	<view class="detail-title">
		<text>标题文本</text>  
	</view>
	<view class="container">
		<scroll-view scroll-y="true">
			<view class="detail-play">
				<image src="../../static/R-C.jpg"></image>
				<view></view>
			</view>
			<view class="detail-icon1">
				<text class="iconfont icon-bofang"></text>
				<text class="iconfont icon-zanting"></text>
			</view>
			<view class="detail-icons">
				<text class="iconfont icon-dianzan"></text>
				<text class="iconfont icon-pinglun" @tap="handleToComment"></text>
				<text class="iconfont icon-fenxiang"></text>
			</view>
		</scroll-view>
		
	</view>
  </view>  
</template>  
  
<script>  
import '@/common/iconfont.css';  
import FMhead1 from '../../components/FMhead1/FMhead1.vue';  
export default {  
  data() {  
    
    
  },  
  components: {
	  FMhead1
  },
  methods :{
  	handleToComment(){
  		uni.navigateTo({
  			url:'/pages/comment/comment'
  		})
  	}
  },
  computed: {  
    
  }  
};  
</script>  
  
<style scoped>  
	.detail-play{
		width:450px;
		height:450px;
		background: url(/static/veer-133025765.jpg);
		background-size: cover;
		margin:200rpx auto 0 auto;
		position: relative;
	}
	
	.detail-play image{
		width:400rpx;
		height: 400rpx;
		border-radius: 50%;
		position: absolute;
		left: 0px;
		top:0;
		right:0;
		bottom:0;
		margin:auto;

	}
	.detail-title{
		font-size: 32rpx;
		margin-top: 170rpx;  
		text-align: center;  
	}
	.detail-icon1{
		font-size: 20rpx;
		margin-top: 10rpx;  
		text-align: center; 
	}
	.detail-icon1 text{
		font-size: 200rpx;
		margin-left: 10rpx;
	}
	 .container {  
	    position: relative; /* 确保子元素可以相对于此元素定位 */  
	  }  
	  
	  .detail-icons {  
	    position: absolute;  
	    top: auto;   
	    bottom: 20rpx;  
	    right: 80rpx;  
	    font-size: 200rpx;   
	    display: flex;   
	    flex-direction: row;   
	  }  
	  
	  .detail-icons text {  
		  font-size: 60rpx;
	    margin-left: 10rpx;   
	  } 
	
</style>