<template>  
  <div class="comment-container">  
    <div class="comment-header">  
      <h2>用户评论</h2>  
    </div>  
      
    <!-- 评论列表 -->  
    <div class="comment-list">  
      <div v-for="(comment, index) in comments" :key="index" class="comment-item">  
        <div class="comment-author">{{ comment.username }}</div>  
        <div class="comment-content">{{ comment.content }}</div>  
        <div class="comment-date">{{ formatDate(comment.date) }}</div>  
      </div>  
      <div v-if="comments.length === 0" class="no-comments">暂无评论</div>  
    </div>  
      
    <!-- 提交评论表单 -->  
    <div class="comment-form">  
      <div class="form-group">  
        <label for="username">用户名</label>  
        <input v-model="newComment.username" type="text" id="username" required>  
      </div>  
      <div class="form-group">  
        <label for="content">评论内容</label>  
        <textarea v-model="newComment.content" id="content" rows="4" required></textarea>  
      </div>  
      <button @click="submitComment" class="submit-btn">提交评论</button>  
    </div>  
  </div>  
</template>  
  
<script>  
export default {  
  data() {  
    return {  
      comments: [  
        // 示例评论数据，实际应从服务器获取  
        { username: '彭于晏', content: '听完很有感悟，让我对当下的处境又有了新的理解，感谢博主！', date: new Date() },  
        { username: '刘亦菲', content: '期待下次更新！', date: new Date(new Date().getTime() - 24 * 60 * 60 * 1000) } // 1天前  
      ],  
      newComment: {  
        username: '',  
        content: ''  
      }  
    };  
  },  
  methods: {  
    formatDate(date) {  
      const options = { year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit' };  
      return new Intl.DateTimeFormat('zh-CN', options).format(date);  
    },  
    submitComment() {  
      if (this.newComment.username && this.newComment.content) {  
        this.comments.push({  
          ...this.newComment,  
          date: new Date()  
        });  
        this.newComment.username = '';  
        this.newComment.content = '';  
      } else {  
        alert('请填写完整的评论信息！');  
      }  
    }  
  }  
};  
</script>  
  
<style scoped>  
.comment-container {  
  max-width: 600px;  
  margin: 0 auto;  
  padding: 20px;  
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);  
  border-radius: 8px;  
  background-color: #fff;  
}  
  
.comment-header {  
  text-align: center;  
  margin-bottom: 20px;  
}  
  
.comment-list {  
  margin-bottom: 20px;  
}  
  
.comment-item {  
  border-bottom: 1px solid #ddd;  
  padding: 15px 0;  
}  
  
.comment-author {  
  font-weight: bold;  
  margin-bottom: 5px;  
}  
  
.comment-content {  
  margin-bottom: 10px;  
}  
  
.comment-date {  
  font-size: 0.875em;  
  color: #666;  
}  
  
.no-comments {  
  text-align: center;  
  color: #999;  
  padding: 15px 0;  
}  
  
.comment-form {  
  display: flex;  
  flex-direction: column;  
}  
  
.form-group {  
  margin-bottom: 15px;  
}  
  
.form-group label {  
  display: block;  
  margin-bottom: 5px;  
  font-weight: bold;  
}  
  
.form-group input,  
.form-group textarea {  
  width: 100%;  
  padding: 10px;  
  font-size: 1em;  
  border: 1px solid #ccc;  
  border-radius: 4px;  
}  
  
.submit-btn {  
  padding: 10px;  
  font-size: 1em;  
  color: #fff;  
  background-color: #007bff;  
  border: none;  
  border-radius: 4px;  
  cursor: pointer;  
  transition: background-color 0.3s;  
}  
  
.submit-btn:hover {  
  background-color: #0056b3;  
}  
</style>