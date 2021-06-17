import requests as req
import logging
import sys


class Asta:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.client = req.session()
        self.logger = logging.getLogger(__name__)

    def login(self):
        LOGIN_URL = 'https://www.e-atoms.jp/ACESPORTSWebUser/Account/LogIn'
        data = {
            'UserName': self.username,
            'Password': self.password,
        }
        self.client.post(LOGIN_URL, data)

    def top_menu(self):
        TOP_URL = 'https://www.e-atoms.jp/ACESPORTSWebUser/'
        res = self.client.get(TOP_URL)
        print(res.text)
        self.logger.info(res.status_code, res.text)

    def inquiry_reserve(self):
        SHOW_RESERVE_URL = 'https://www.e-atoms.jp/ACESPORTSWebUser/YYS/Reserve'
        self.client.get(SHOW_RESERVE_URL)
        INQUIRY_RESERVE_URL = 'https://www.e-atoms.jp/ACESPORTSWebUser/YYS/Reserve/InquiryReserve'
        data = {
            'tmpoCD': '001',
            'day': '20210617',
            'sisetuGrpCD': '00001',
            'sisetuCD': '00001',
            'ExecuteType': 'ChangeCond',
        }
        res = self.client.post(INQUIRY_RESERVE_URL, data)
        print(res.text)
        # self.logger.warning(res.status_code, res.text)


username = sys.argv[1]
password = sys.argv[2]
asta = Asta(username, password)
asta.login()
asta.inquiry_reserve()
