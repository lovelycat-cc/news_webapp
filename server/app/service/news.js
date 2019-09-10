const Service = require('egg').Service

class NewsService extends Service {
    async list(page, label) {
        const {ctx} = this
        const { pageSize } = this.config.news
        let count = await ctx.model.News.find({label: label}).countDocuments()
        const data = await ctx.model.News.find({label: label}, {content: 0}).skip((page - 1) * pageSize).limit(pageSize) // content设为0，则不获取content数据
        return { count, data }
    }
}

module.exports = NewsService