import httplib, json, urllib, time, os

SEARCH = "#donaldtrump OR #trump OR #trump2016 OR #trumpforpresident"
FOLDER = "data"
B64 = "XXX" #create your own API key to use this program
ADDRESS = "/1.1/search/tweets.json"

class Crawl:
    def __init__(self):
        self.conn = httplib.HTTPSConnection("api.twitter.com")
        self.b64token = B64
        self.search = SEARCH
        self.folder = FOLDER
        self.bearer = self.connect()
        self.next = ""

    def connect(self):
        headers = {"Content-type":"application/x-www-form-urlencoded","Authorization":"Basic "+self.b64token}
        self.conn.request("POST", "/oauth2/token", "grant_type=client_credentials", headers)
        return json.load(self.conn.getresponse()).get("access_token")

    def run(self):
        while self.crawl() == True:
            time.sleep(3)
        self.conn.close()


    def crawl(self):
        if self.next=="":
            params = {"q":SEARCH,"result_type":"recent", "count":100, "include_entities":False}
        headers = {"Authorization":"Bearer "+self.bearer}
        self.conn.request("GET", ADDRESS+(("?"+urllib.urlencode(params)) if (self.next=="") else self.next),"", headers)
        resp =  self.conn.getresponse().read()
        arr = json.loads(resp)
        if "errors" in arr:
            return False
        if "next_results" not in arr["search_metadata"]:
            min = arr["search_metadata"]["max_id"]
            for tweet in arr["statuses"]:
                if tweet["id"] < min:
                    min = tweet["id"]
                self.parse_and_save(tweet)
            self.next = "?" + urllib.urlencode({"q":SEARCH,"result_type":"recent", "count":100, "include_entities":False, "max_id":min})
        else:
            self.next = arr["search_metadata"]["next_results"]
            for tweet in arr["statuses"]:
                self.parse_and_save(tweet)
        return True

    def parse_and_save(self,tweet):
        id = tweet["id_str"]
        f = open(os.path.join(self.folder,"json", id+".json"), mode="w")
        json.dump(tweet, f)
        f.close()
        f = open(os.path.join(self.folder, id+".txt"), mode="w")
        f.write(tweet["text"].encode('utf-8'))
        f.close()


if __name__ == "__main__":
    crawl = Crawl()
    crawl.run()