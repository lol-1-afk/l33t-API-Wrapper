import requests
import simplejson


class ApiWrapper:
    def __init__(self, captcha_key: str):
        if len(captcha_key) != 32:
            raise Exception("Invalid captcha key!")

        self.api_key = captcha_key
        self.base_url = "http://api.l33t.ltd"

    def make_request(self, sub_url: str, params: dict = None):
        """
        :param sub_url: sub url where request will be send
        :param params: dict of parametrs to send
        stupid site with stuped certificate, post method for captcha and get for other
        reurns result of request
        """
        if params is None:
            params = {}
        params.update({"key": self.api_key})

        if "method" not in params:
            get_resnponse = requests.get(self.base_url + sub_url, params=params)
        else:
            get_resnponse = requests.post(self.base_url + sub_url, data=params)

        if "json" in params and params["json"] == 1:
            try:
                return get_resnponse.json()
            except simplejson.errors.JSONDecodeError:
                return {"error": get_resnponse.text}
        else:
            return get_resnponse.text

    def get_key(self):
        """
        returns actual api key
        """
        return self.api_key

    def update_key(self, captcha_key: str):
        """
        :param captcha_key: new api key
        updates api key
        """
        if len(captcha_key) != 32:
            raise Exception("Invalid captcha key!")

        self.api_key = captcha_key

    def get_balance(self):
        """
        returns api key balance in rubles
        """
        balance = self.make_request(
            sub_url="/res.php", params={"action": "getbalance"}
        )
        return balance

    def get_threads(self):
        """
        returns all threads count
        """
        threads_count = self.make_request(
            sub_url="/getthreads",
        )
        return threads_count

    def get_free_threads(self):
        """
        returns free threads count
        """
        free_threads_count = self.make_request(
            sub_url="/freethreads"
        )
        return free_threads_count

    def get_cap_answer(self, cap_id, is_json: int = 0):
        """
        :param cap_id: captcha solution id
        :param is_json: returns json dict if 1, else string
        :return:
        """
        get_answer = self.make_request(
            sub_url="/res.php",
            params={"action": "get", "id": cap_id, "json": is_json}
        )
        return get_answer

    def solve_recaptcha(self, cap_version: int, page_url: str, sitekey: str = None, k_value: str = None,
                        min_score: int = None, cookies: str = None, user_agent: str = None, dev_id: int = None,
                        is_json: int = 0, proxy: str = None, proxy_type: str = None, data_s: str = None):
        """
        :param cap_version: captcha version: 2 or 3
        :param page_url: url where captcha is needed
        :param sitekey: sitekey from web site
        :param k_value: k value from website if sitekey is not found
        :param min_score: minimal score value, default 0.1
        :param cookies: KEY1:Value1;KEY2:Value2
        :param user_agent: useragent
        :param dev_id: soft developer's id
        :param is_json: returns json dict if 1, else string
        :param proxy: username:password@ip:port
        :param proxy_type: HTTP, HTTPS, SOCKS4, SOCKS5
        :param data_s: data-s value from web page

        this function sends values to server, than returns solution id
        """

        if cap_version not in [2, 3]:
            raise Exception("cap_version can be only 2 for recaptcha2 and 3 for recaptcha3")

        if sitekey is None and k_value is None:
            raise Exception("sitekey or k_value must be specified!")

        params = {"method": "userrecaptcha", "googlekey": sitekey or k_value, "pageurl": page_url,
                  "cookies": cookies, "userAgent": user_agent, "l3soft": dev_id, "json": is_json,
                  "proxy": proxy, "proxytype": proxy_type}

        if cap_version == 2:
            params.update({"data-s": data_s})
        else:
            params.update({"version": "v3", "min_score": min_score})

        send_cap = self.make_request(
            sub_url="/in.php",
            params=params
        )
        return send_cap

    def solve_imgcaptcha(self, captcha_str: str, is_json: int = 0):
        """
        :param captcha_str: base64 string of captcha image
        :param is_json: returns json dict if 1, else string
        """
        params = {"method": "base64", "body": captcha_str, "json": is_json}
        send_cap = self.make_request(
            sub_url="/in.php",
            params=params
        )
        return send_cap

