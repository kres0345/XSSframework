### Does not work
import urllib.request
#url = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'
def replace_between(text, begin, end, alternative=''):
    middle = text.split(begin, 1)[1].split(end, 1)[0]
    return text.replace(middle, alternative)
def checkPayloads():
    print("Checking for updates...")
    url = "https://github.com/kres0345/XSSframework/tree/master/Payloads"
    urllib.request.urlretrieve(url, 'tmp\\PayloadsNew.website')
    NewPayloads = open("tmp\\PayloadsNew.website", "r").read()
    OldPayloads = open("tmp\\PayloadsOld.website", "r").read()
    #Start NewPayloads
    middle = NewPayloads.split('<meta name="request-id"', 1)[1].split('data-pjax-transient>', 1)[0]
    NewPayloads = NewPayloads.replace(middle, "")
    middle = NewPayloads.split('<meta content="collector.githubapp.com"', 1)[1].split('name="octolytics-dimension-region_render" />', 1)[0]
    NewPayloads = NewPayloads.replace(middle, "")
    middle = NewPayloads.split('<meta name="js-proxy-site-detection-payload"', 1)[1].split('">', 1)[0]
    NewPayloads = NewPayloads.replace(middle, "")
    middle = NewPayloads.split('<meta name="html-safe-nonce"', 1)[1].split('">', 1)[0]
    NewPayloads = NewPayloads.replace(middle, "")
    middle = NewPayloads.split('<li class="mr-3">&', 1)[1].split('Inc.</li>', 1)[0]
    NewPayloads = NewPayloads.replace(middle, "")
    #end removing some text
    #Start newpayloads
    middle = OldPayloads.split('<meta name="request-id"', 1)[1].split('data-pjax-transient>', 1)[0]
    OldPayloads = OldPayloads.replace(middle, "")
    middle = OldPayloads.split('<meta content="collector.githubapp.com"', 1)[1].split('name="octolytics-dimension-region_render" />', 1)[0]
    OldPayloads = OldPayloads.replace(middle, "")
    middle = OldPayloads.split('<meta name="js-proxy-site-detection-payload"', 1)[1].split('">', 1)[0]
    OldPayloads = OldPayloads.replace(middle, "")
    middle = OldPayloads.split('<meta name="html-safe-nonce"', 1)[1].split('">', 1)[0]
    OldPayloads = OldPayloads.replace(middle, "")
    middle = OldPayloads.split('<li class="mr-3">&', 1)[1].split('Inc.</li>', 1)[0]
    OldPayloads = OldPayloads.replace(middle, "")
    #end oldpayloads
    #open("test.website", "w").write(NewPayloads)
    if (NewPayloads != OldPayloads):
        url = "https://github.com/kres0345/XSSframework/tree/master/Payloads"
        urllib.request.urlretrieve(url, 'tmp\\PayloadsOld.website')
        print("New Payloads discovered, updating.")
    else:
        print("No new Payloads discovered.")
def checkMethods():
    print("Checking for updates...")
    url = "https://github.com/kres0345/XSSframework/tree/master/Methods"
    urllib.request.urlretrieve(url, 'tmp\\MethodNew.website')
    NewMethods = open("tmp\\MethodsNew.website", "r").read()
    OldMethods = open("tmp\\MethodsOld.website", "r").read()
    #Start NewMethods
    middle = NewMethods.split('<meta name="request-id"', 1)[1].split('data-pjax-transient>', 1)[0]
    NewMethods = NewMethods.replace(middle, "")
    middle = NewMethods.split('<meta content="collector.githubapp.com"', 1)[1].split('name="octolytics-dimension-region_render" />', 1)[0]
    NewMethods = NewMethods.replace(middle, "")
    middle = NewMethods.split('<meta name="js-proxy-site-detection-payload"', 1)[1].split('">', 1)[0]
    NewMethods = NewMethods.replace(middle, "")
    middle = NewMethods.split('<meta name="html-safe-nonce"', 1)[1].split('">', 1)[0]
    NewMethods = NewMethods.replace(middle, "")
    middle = NewMethods.split('<li class="mr-3">&', 1)[1].split('Inc.</li>', 1)[0]
    NewMethods = NewMethods.replace(middle, "")
    #end removing some text
    #Start newMethods
    middle = OldMethods.split('<meta name="request-id"', 1)[1].split('data-pjax-transient>', 1)[0]
    OldMethods = OldMethods.replace(middle, "")
    middle = OldMethods.split('<meta content="collector.githubapp.com"', 1)[1].split('name="octolytics-dimension-region_render" />', 1)[0]
    OldMethods = OldMethods.replace(middle, "")
    middle = OldMethods.split('<meta name="js-proxy-site-detection-payload"', 1)[1].split('">', 1)[0]
    OldMethods = OldMethods.replace(middle, "")
    middle = OldMethods.split('<meta name="html-safe-nonce"', 1)[1].split('">', 1)[0]
    OldMethods = OldMethods.replace(middle, "")
    middle = OldMethods.split('<li class="mr-3">&', 1)[1].split('Inc.</li>', 1)[0]
    OldMethods = OldMethods.replace(middle, "")
    #end oldMethods
    #open("test.website", "w").write(NewPayloads)
    if (NewPayloads != OldPayloads):
        url = "https://github.com/kres0345/XSSframework/tree/master/Payloads"
        urllib.request.urlretrieve(url, 'tmp\\PayloadsOld.website')
        print("New Payloads discovered, updating.")
    else:
        print("No new Payloads discovered.")
    
