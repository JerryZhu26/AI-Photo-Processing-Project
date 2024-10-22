<template>  
  <view class="FM-buttom-container">  
    <view class="icon-wrapper">  
      <text class="iconfont icon-xiaoyuzhou"></text>  
      <text class="icon-text">发现</text>  
    </view>  
    <view class="icon-wrapper">  
      <text class="iconfont icon-wodedingyue"></text>  
      <text class="icon-text">订阅</text>  
    </view>  
    <view class="icon-wrapper">  
      <text class="iconfont icon-geren"></text>  
      <text class="icon-text">个人</text>  
    </view>  
  </view>  
</template>  
  
<script>  
export default {  
  name: "FMbuttom",  
  data() {  
    return {};  
  }  
};  
</script>  
  
<style scoped>  
.FM-buttom-container {  
  position: fixed;   
  bottom: 0;   
  left: 0;   
  right: 0;   
  display: flex;  
  justify-content: space-around;   
  align-items: flex-end;   
  background-color: white;   
  padding: 10px;  
  box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.1);   
}  
  
.icon-wrapper {  
  display: flex;  
  flex-direction: column;  
  align-items: center;  
  text-align: center;   
}  
  
.icon-text {  
  margin-top: 5px;   
  font-size: 14px;   
}  
  
.iconfont {  
  font-size: 24px;   
}  
</style>