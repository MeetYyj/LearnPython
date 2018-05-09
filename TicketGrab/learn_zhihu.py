from splinter.browser import Browser

if __name__ == '__main__':
    x = Browser(driver_name="chrome")
    url = "https://www.baidu.com"
    x.visit(url)
    x.fill("wd", "hello world")
    x.find_by_id("su").click()
