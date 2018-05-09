from splinter.browser import Browser

if __name__ == '__main__':
    x = Browser(driver_name="chrome")
    url = "https://www.meituan.com"
    x.visit(url)
    x.find_by_text(u"登录").click()
    x.fill("email", "username")
    x.fill("password", "password")
    x.find_by_name("commit").click()
