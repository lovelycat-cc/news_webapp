<template>
<div class="news-list">
  <swiper 
    class="swiper swiper-container" 
    :indicator-dots="true" 
    interval="5000" 
    duration="1000" 
    autoplay>
    <block v-for="(item, index) in banners" :index="index" :key="index">
        <swiper-item>
            <img :src="item.src" class="swiper-slide"/>
        </swiper-item>
    </block>
  </swiper>
  <scroll-view scroll-x class="scroll-view" :scroll-left="scrollLeft" scroll-with-animation>
    <view 
      v-for="(item, index) in labels" 
      :key="index" class="view-item" 
      @click="tabClick(index, item)" 
      :class="{'active': item.name === currentName}"
    >
      {{item.label}}
    </view>
  </scroll-view>
  <div class="news-list" v-for="(item, index) in newsList" :key="index">
    <div class="left">
      <img :src="item.imgurl"/>
    </div>
    <div class="right">
      <p>{{item.title}}</p>
      <div class="tags">
        <span class="tag" v-for="(i, idx) in item.keywords" :key="idx">{{i.keyname}}</span>
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  data () {
    return {
      labels: [
        {
          label: '要闻',
          name: 'keynews'
        },
        {
          label: '国内',
          name: 'country'
        },
        {
          label: '国际',
          name: 'international'
        },
        {
          label: '军事',
          name: 'military'
        },
        {
          label: '财经',
          name: 'money'
        },
        {
          label: '科技',
          name: 'technique'
        }
      ],
      banners: [
        {
          src: '/static/images/banner-1.jpg'
        }, {
          src: '/static/images/banner-2.jpg'
        }, {
          src: '/static/images/banner-3.jpg'
        }
      ],
      scrollLeft: 0,
      currentLabel: '要闻',
      currentName: 'keynews',
      newsList: [],
      page: 1
    }
  },
  methods: {
    tabClick (index, item) {
      if (index >= 3) {
        this.scrollLeft = (index - 2) * 66
      } else {
        this.scrollLeft = 0
      }
      this.currentName = item.name
      this.page = 1
      this.currentLabel = item.label
      this.getList(true)
    },
    getList (refresh) {
      this.$axios.get(`/news?page=${this.page}&label=${this.currentLabel}`).then(res => {
        if (refresh) {
          this.newsList = res.data.data
        } else {
          this.newsList = this.newsList.concat(res.data.data)
        }
      }).catch(e => {
        console.log(e)
      })
    }
  },
  onReachBottom () {
    this.page++
    this.getList()
  },
  async onPullDownRefresh () {
    this.page = 1
    this.getList(true)
  },
  mounted () {
    console.log('mounted')
    this.getList(true)
  }
}
</script>

<style scoped>
.swiper {
  height: 400rpx;
}
.swiper-slide {
  width: 750rpx;
}
.scroll-view {
  white-space: nowrap;
}
.view-item {
  display: inline-block;
  height: 80rpx;
  line-height: 80rpx;
  padding: 0 40rpx;
  cursor: pointer;
}
.view-item.active {
  border-bottom: 3rpx solid #e81f1f;
  box-sizing: border-box;
}
.news-list .left img {
  width: 750rpx;
}
.tags {
  margin: 10rpx 0 10rpx;
  text-align: right;
}
.tags .tag {
  padding: 5rpx;
  border: 1rpx solid #e81f1f;
  margin-right: 4rpx;
  border-radius: 5rpx;
}
</style>
