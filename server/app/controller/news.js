const Controller = require('egg').Controller

class NewsController extends Controller {
    async list() {
        const { ctx } = this
        const page = ctx.query.page || 1
        const label = ctx.query.label || '要闻'
        let newsList = await ctx.service.news.list(page, label)
        this.ctx.body = newsList
    }
}

module.exports = NewsController