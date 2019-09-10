exports.keys = '123'

exports.news = {
    pageSize: 10
}

exports.cors = {
    origin: '*',
    allowMethods: 'GET, HEAD, PUT, POST, DELETE, PATCH'
}

exports.mongoose = {
    client:{
        url: 'mongodb://admin:123321@127.0.0.1:27017/admin', // 连入admin数据库
        options: {}
    }
}