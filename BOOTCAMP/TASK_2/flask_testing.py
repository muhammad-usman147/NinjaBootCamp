import unittest
from flask_sql import app

class FlaskSqlTesting(unittest.TestCase):
    def test_getapi(self):
        tester = app.test_client(self)
        response = tester.get('/getapi',content_type = 'html/text')
        self.assertEqual(response.status_code,200)
    def test_getsingleapi(self):
        tester = app.test_client(self)
        response = tester.get('/getsingleapi/12345',content_type = 'html/text')
        self.assertEqual(response.status_code,200)
    def test_postapi(self):
        tester = app.test_client(self)
        response = tester.post('/postapi/888/Kings/KingOfPaksitan/True',content_type = 'html/text')
        self.assertEqual(response.status_code,200)
    def test_putapi(self):
        tester = app.test_client(self)
        response = tester.put('/putapi/888/title/WrestleMania',content_type = 'html/text')
        self.assertEqual(response.status_code,200)
    def test_deleteapi(self):
        tester = app.test_client(self)
        response = tester.delete('/deleteapi/888',content_type = 'html/text')
        self.assertEqual(response.status_code,200)
if __name__ == '__main__':
    unittest.main()