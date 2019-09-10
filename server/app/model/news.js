module.exports = app => {
    const mongoose = app.mongoose
    const Schema = mongoose.Schema
    const NewsSchema = new Schema({
        _id: {
            type: Schema.ObjectId
        },
        title: {
            type: String
        },
        content: {
            type: String
        },
        source: {
            type: String
        },
        publish_time: {
            type: String
        },
        keywords: {
            type: Array
        },
        imgurl: {
            type: String
        },
        label: {
            type: String
        }
    })

    return mongoose.model('News', NewsSchema) // 对应集合名为news
}