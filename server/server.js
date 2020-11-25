var http = require('http')
var fs = require('fs')

http
	.createServer((req, res) => {
		fs.readFile('fake.json', (err, data) => {
			res.writeHead(200, {
				'Access-Control-Allow-Origin': '*',
				'Access-Control-Allow-Headers': 'X-Requested-With',
			})
			if (err) {
				res.write('server error')
			} else {
				res.write(data)
			}
			res.end()
		})
	})
	.listen(3000)
