<template>
  <div>
    <div class="userinfo">
      <img class="userinfo-avatar" src="/static/images/user.png" background-size="cover" />
      <div class="userinfo-nickname">
       {{userInfo.nickName}}
      </div>
    </div>
    <div  class="btn">
      <i-button @click="bindViewTap">进入小程序</i-button>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      userInfo: {
        nickName: 'ccnews'
      }
    }
  },
  methods: {
    bindViewTap () {
      const url = '../newsList/main'
      if (mpvuePlatform === 'wx') {
        mpvue.switchTab({ url })
      } else {
        mpvue.navigateTo({ url })
      }
    }
  },

  created () {
    // let app = getApp()
  }
}
</script>

<style scoped>
.userinfo {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.userinfo-avatar {
  width: 180rpx;
  height: 180rpx;
  margin-top: 200rpx;  
}
.btn {
  margin: 0 auto;
  margin-top: 180rpx;
  width: 500rpx;
}
</style>
