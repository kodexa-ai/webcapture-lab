from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver import ChromeOptions, Chrome
from helium import *

driver_manager = ChromeDriverManager()
set_driver(Chrome(driver_manager.install()))

# Start your script below here

go_to('https://ww2.salliemae.com/investors/asset-backed-securities/smb/2017-a/')

print("Clicking buttons")
for btn in find_all(S('.cmp-accordion__button')):
    print("Clicking btn")
    click(btn)

# Lets just grab all the PDF links
print("Clicking links")

for link in find_all(S('a[href$=".pdf"]')):
    click(link)
    break


# End your script before this
get_driver().close()