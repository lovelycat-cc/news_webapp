import Vue from 'vue'
import axios from 'axios'
import App from './App'
import SERVICE_URL from './../static/urlconfig.js'

Vue.prototype.$axios = axios
axios.defaults.baseURL = SERVICE_URL

axios.defaults.adapter = function (config) {
  return new Promise((resolve, reject) => {
    let con = {
      method: config.method,
      url: config.url,
      header: config.headers,
      success (res) {
        resolve(res)
      },
      fail (res) {
        reject(res)
      }
    }
    // 调用微信接口发出请求
    wx.request(con)
  })
}
Vue.config.productionTip = false
App.mpType = 'app'

const app = new Vue(App)
app.$mount()
