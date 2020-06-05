'''
Instructions

Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
'''
#CODE
def domain_name(url):
    from re import findall
    return findall('(?:https:\/\/)?(?:http:\/\/)?(?:www\.)?([\w\W]+?)(?:\.)', url)[0]
