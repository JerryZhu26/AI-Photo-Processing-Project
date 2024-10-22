<template>  
	<view class="index">  
		<FMhead title="发现" class="fm-head-custom"></FMhead>  
		<view class="container">  
			<scroll-view scroll-y="true" class="scroll-view-custom">  
				<view class="index-head">  
					<text class="index-head-text">发现</text>  
					<text class="iconfont icon-xiaoyuzhou index-head-icon"></text>  
				</view>  
				<view class="index-search">  
					<text class="iconfont icon-sousuo"></text>  
					<input type="text" placeholder="搜索电台" />  
					<text class="iconfont icon-saoma"></text>  
				</view>  
				<view class="index-list">  
					<view class="index-list-item">  
						<view class="index-list-content">  
							<view class="index-list-title">  
								<text>标题文本</text>  
							</view>  
							<view class="index-list-img">  
								<img src="../../static/R-C.jpg" alt="" />  
							</view>  
							<view class="index-list-description">  
								<text>这是简介文本。</text>  
							</view>  
						</view>  
						<view class="index-list-icons">  
							<text class="iconfont icon-jiarugedan"></text>  
							<text class="iconfont icon-bofang" @tap="handleToDetail"></text>  
						</view>  
						<view class="index-list-ellipsis">
							<text class="iconfont icon-ellipsis"></text>
						</view>
					</view>  
				</view>  
				<view class="index-list">
					<view class="index-list-item">  
						<view class="index-list-content">  
							<view class="index-list-title">  
								<text>标题文本</text>  
							</view>  
							<view class="index-list-img">  
								<img src="../../static/R-C.jpg" alt="" />  
							</view>  
							<view class="index-list-description">  
								<text>这是简介文本。</text>  
							</view>  
						</view>  
						<view class="index-list-icons">  
							<text class="iconfont icon-jiarugedan"></text>  
							<text class="iconfont icon-bofang" @tap="handleToDetail"></text>  
						</view>  
						<view class="index-list-ellipsis">
							<text class="iconfont icon-ellipsis"></text>
						</view>
					</view>  
				</view>  
				<view class="index-list">
					<view class="index-list-item">  
						<view class="index-list-content">  
							<view class="index-list-title">  
								<text>标题文本</text>  
							</view>  
							<view class="index-list-img">  
								<img src="../../static/R-C.jpg" alt="" />  
							</view>  
							<view class="index-list-description">  
								<text>这是简介文本。</text>  
							</view>  
						</view>  
						<view class="index-list-icons">  
							<text class="iconfont icon-jiarugedan"></text>  
							<text class="iconfont icon-bofang" @tap="handleToDetail"></text>  
						</view>  
						<view class="index-list-ellipsis">
							<text class="iconfont icon-ellipsis"></text>
						</view>
					</view>  
				</view>  
				<view class="index-list">
					<view class="index-list-item">  
						<view class="index-list-content">  
							<view class="index-list-title">  
								<text>标题文本</text>  
							</view>  
							<view class="index-list-img">  
								<img src="../../static/R-C.jpg" alt="" />  
							</view>  
							<view class="index-list-description">  
								<text>这是简介文本。</text>  
							</view>  
						</view>  
						<view class="index-list-icons">  
							<text class="iconfont icon-jiarugedan"></text>  
							<text class="iconfont icon-bofang" @tap="handleToDetail"></text>  
						</view>  
						<view class="index-list-ellipsis">
							<text class="iconfont icon-ellipsis"></text>
						</view>
					</view>  
				</view>  
				<view class="index-list">
					<view class="index-list-item">  
						<view class="index-list-content">  
							<view class="index-list-title">  
								<text>标题文本</text>  
							</view>  
							<view class="index-list-img">  
								<img src="../../static/R-C.jpg" alt="" />  
							</view>  
							<view class="index-list-description">  
								<text>这是简介文本。</text>  
							</view>  
						</view>  
						<view class="index-list-icons">  
							<text class="iconfont icon-jiarugedan"></text>  
							<text class="iconfont icon-bofang" @tap="handleToDetail"></text>  
						</view>  
						<view class="index-list-ellipsis">
							<text class="iconfont icon-ellipsis"></text>
						</view>
					</view>  
				</view>  
				<view class="index-list">
					<view class="index-list-item">  
						<view class="index-list-content">  
							<view class="index-list-title">  
								<text>标题文本</text>  
							</view>  
							<view class="index-list-img">  
								<img src="../../static/R-C.jpg" alt="" />  
							</view>  
							<view class="index-list-description">  
								<text>这是简介文本。</text>  
							</view>  
						</view>  
						<view class="index-list-icons">  
							<text class="iconfont icon-jiarugedan"></text>  
							<text class="iconfont icon-bofang" @tap="handleToDetail"></text>  
						</view>  
						<view class="index-list-ellipsis">
							<text class="iconfont icon-ellipsis"></text>
						</view>
					</view>  
				</view>  
				<view class="index-list">
					<view class="index-list-item">  
						<view class="index-list-content">  
							<view class="index-list-title">  
								<text>标题文本</text>  
							</view>  
							<view class="index-list-img">  
								<img src="../../static/R-C.jpg" alt="" />  
							</view>  
							<view class="index-list-description">  
								<text>这是简介文本。</text>  
							</view>  
						</view>  
						<view class="index-list-icons">  
							<text class="iconfont icon-jiarugedan"></text>  
							<text class="iconfont icon-bofang" @tap="handleToDetail"></text>  
						</view>  
						<view class="index-list-ellipsis">
							<text class="iconfont icon-ellipsis"></text>
						</view>
					</view>  
				</view>  
				
				
			</scroll-view>  
		</view>  
		<FMbuttom class="fm-buttom-custom"></FMbuttom>  
	</view>  
</template>  
  
<script>  
	import '@/common/iconfont.css';  
	import FMhead from '../../components/FMhead/FMhead.vue';  
	export default {  
		data() {  
			return {};  
		},  
		components: {  
			FMhead,  
		},  
		onLoad() {},  
		methods: {
			handleToDetail(){
				uni.navigateTo({
					url:'/pages/detail/detail'
				})
			}
		},  
	};  
</script>  
  
<style scoped>  
	.index {}  
	.index-search {  
		display: flex;  
		align-items: center;  
		height: 70rpx;  
		margin: 70rpx 30rpx 30rpx 30rpx;  
		background: #f7f7f7;  
		border-radius: 50rpx;  
	}  
	.index-search text {  
		font-size: 26rpx;  
		margin-right: 26rpx;  
		margin-left: 28rpx;  
	}  
	.index-search input {  
		font-size: 28rpx;  
		flex: 1;  
	}  
	.index-head {  
		display: flex;  
		align-items: center;  
		height: 100rpx;  
		margin: 30rpx 30rpx 30rpx 30rpx;  
		justify-content: space-between;  
	}  
	.index-head-text {  
		font-size: 60rpx;  
	}  
	.index-head-icon {  
		font-size: 100rpx;  
		color: cornflowerblue;  
	}  
	.index-list {  
		margin: 0 30rpx;  
	}  
	.index-list-item {  
		display: flex;  
		flex-direction: column;  
		align-items: center;  
		justify-content: space-between;   
		margin-bottom: 34rpx;  
		background: #f7f7f7;  
		border-radius: 50rpx;  
		padding: 20rpx;  
		position: relative;  
	}  
	.index-list-content {  
		flex: 1;   
		display: flex;  
		flex-direction: column;  
		align-items: center;   
		justify-content: center; 
	}  
	.index-list-title {  
		font-size: 32rpx;  
		margin-bottom: 10rpx;  
		text-align: center;  
	}  
	.index-list-img img {  
		max-width: 100%;   
		max-height: 200rpx;   
		object-fit: contain;   
	}  
	.index-list-description {  
		font-size: 28rpx;  
		margin-top: 10rpx;  
		text-align: center;  
	}  
	.index-list-icons {  
		position: absolute;   
		bottom: 20rpx;   
		right: 20rpx;   
		display: flex;  
		align-items: center;  
	}  
	.index-list-icons text {  
		font-size: 50rpx;   
		margin-left: 10rpx;   
	}  
	.index-list-ellipsis {  
			position: absolute;   
			top: 20rpx;   
			right: 20rpx;   
			display: flex;  
			align-items: center;  
		}  
		.index-list-ellipsis text {  
			font-size: 50rpx;   
			color: #999999;   
		}  
		.fm-head-custom {  
		    height: 80px;   
		  }  
		  
		  .fm-buttom-custom {  
		    height: 80px;   
		    position: fixed;   
		    bottom: 0;   
		    left: 0;   
		    right: 0;   
		  }  
		  .scroll-view-custom {    
		      padding-top: 80px;  
		      padding-bottom: 80px;
		    }  
</style>