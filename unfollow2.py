from selenium import webdriver
from time import sleep
from secrets import username, pw


class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")\
            .click()
        sleep(2)

    def get_unfollowers(self):
        self.driver.get(f'https://instagram.com/{username}')

        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        sleep(2)
        following = self._get_names()
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()
        followers = self._get_names()

        not_following_back = [user for user in following if user not in followers]
        #print(not_following_back)
        for C in not_following_back:
            self.driver.get(f'https:/instagram.com/{C}')
            sleep(5)
            self.driver.find_element_by_class_name('_5f5mN.-fzfL._6VtSN.yZn4P')\
                .click()
            self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]')\
                .click()
            sleep(1)

# You can enable these code to list the name of the persons who are not following you back
            #print ('There are', len(not_following_back), 'people not following you back')
            #print('list of not following:', C)


    def _get_names(self):
        #sleep(2)
        #sugs = self.driver.find_element_by_xpath('//h4[contains(text(), Suggestions)]')
        #self.driver.execute_script('arguments[0].scrollIntoView()')
        #sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        people = len(names)
        # close button
        self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button")\
            .click()
        return names
        



my_bot = InstaBot(username, pw)
my_bot.get_unfollowers()

