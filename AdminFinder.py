import requests
from bs4 import BeautifulSoup
import re
import argparse

BANNER = """
\033[38;5;198m  ___      _           _      \033[38;5;93m______ _           _           
\033[38;5;197m / _ \\    | |         (_)     \033[38;5;99m|  ___(_)         | |          
\033[38;5;203m/ /_\\\\ \\ __| |_ __ ___  _ _ __ \033[38;5;105m| |_   _ _ __   __| | ___ _ __ 
\033[38;5;210m|  _  |/ _` | '_ ` _ \\| | '_ \\ \033[38;5;111m|  _| | | '_ \\ / _` |/ _ \\ '__|
\033[38;5;215m| | | | (_| | | | | | | | | | |\033[38;5;117m| |   | | | | | (_| |  __/ |   
\033[38;5;221m\\_| |_/\\__,_|_| |_| |_|_|_| |_|\033[38;5;123m\\_|   |_|_| |_|\\__,_|\\___|_|   

\033[38;5;51mAuthor: \033[1mG4UR4V007\033[0m
\033[38;5;47mVersion: 1.0\033[0m
"""
def success(msg): print(f"\033[92m[+]\033[0m {msg}")
def info(msg): print(f"\033[94m[*]\033[0m {msg}")
def error(msg): print(f"\033[91m[-]\033[0m {msg}")

admin_panel_urls = [
    '/administrator/', '/admin1/', '/admin2/', '/admin3/', '/admin4/', '/admin5/',
    '/usuarios/', '/usuario/', '/moderator/', '/webadmin/', '/adminarea/',
    '/bb-admin/', '/adminLogin/', '/admin_area/', '/panel-administracion/', '/admin/',
    '/instadmin/', '/memberadmin/', '/administratorlogin/', '/adm/', '/admin/account.php',
    '/admin/index.php', '/admin/login.php', '/admin/admin.php', '/admin_area/admin.php',
    '/admin_area/login.php', '/siteadmin/login.php', '/siteadmin/index.php',
    '/siteadmin/login.html', '/admin/account.html', '/admin/index.html',
    '/admin/login.html', '/admin/admin.html', '/admin_area/index.php', '/bb-admin/index.php',
    '/bb-admin/login.php', '/bb-admin/admin.php', '/admin/home.php',
    '/admin_area/login.html', '/admin_area/index.html', '/admin/controlpanel.php',
    '/admin.php', '/admincp/index.asp', '/admincp/login.asp', '/admincp/index.html',
    '/adminpanel.html', '/webadmin.html', '/webadmin/index.html', '/webadmin/admin.html',
    '/webadmin/login.html', '/admin/admin_login.html', '/admin_login.html',
    '/panel-administracion/login.html', '/admin/cp.php', '/cp.php', '/administrator/index.php',
    '/administrator/login.php', '/nsw/admin/login.php', '/webadmin/login.php',
    '/admin/admin_login.php', '/admin_login.php', '/administrator/account.php',
    '/administrator.php', '/pages/admin/admin-login.php', '/admin/admin-login.php',
    '/admin-login.php', '/acceso.php', '/admin/home.html', '/login.php',
    '/modelsearch/login.php', '/moderator.php', '/moderator/login.php',
    '/moderator/admin.php', '/account.php', '/controlpanel.php', '/admincontrol.php',
    '/admin/adminLogin.html', '/rcjakar/admin/login.php', '/adminarea/index.html',
    '/adminarea/admin.html', '/webadmin.php', '/webadmin/index.php', '/webadmin/admin.php',
    '/admin/controlpanel.html', '/admin.html', '/admin/cp.html', '/cp.html',
    '/moderator.html', '/administrator/index.html', '/administrator/login.html',
    '/user.html', '/administrator/account.html', '/administrator.html', '/login.html',
    '/modelsearch/login.html', '/moderator/login.html', '/adminarea/login.html',
    '/panel-administracion/index.html', '/panel-administracion/admin.html',
    '/modelsearch/index.html', '/modelsearch/admin.html', '/admincontrol/login.html',
    '/adm/index.html', '/adm.html', '/moderator/admin.html', '/user.php', '/account.html',
    '/controlpanel.html', '/admincontrol.html', '/panel-administracion/login.php',
    '/wp-login.php', '/adminLogin.php', '/admin/adminLogin.php', '/home.php',
    '/adminarea/index.php', '/adminarea/admin.php', '/adminarea/login.php',
    '/panel-administracion/index.php', '/panel-administracion/admin.php',
    '/modelsearch/index.php', '/modelsearch/admin.php', '/admincontrol/login.php',
    '/adm/admloginuser.php', '/admloginuser.php', '/admin2.php', '/admin2/login.php',
    '/admin2/index.php', '/usuarios/login.php', '/adm/index.php', '/adm.php',
    '/affiliate.php', '/adm_auth.php', '/memberadmin.php', '/administratorlogin.php'
]

def normalize_url(url):
    return url if url.endswith('/') else url + '/'

def get_wordlist(url):
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=5)
        response.raise_for_status()
    except requests.RequestException as e:
        error(f"Error fetching the URL: {e}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    words = re.findall(r'\b\w+\b', soup.get_text())
    return list(set(words))

def find_admin_panel(url):
    print(BANNER)
    url = normalize_url(url)
    info(f"Scanning URL: {url}")

    wordlist = get_wordlist(url)

    for admin_url in admin_panel_urls:
        full_url = url + admin_url.lstrip('/')
        try:
            response = requests.get(full_url, headers={"User-Agent": "Mozilla/5.0"}, timeout=5)
            if response.status_code == 200:
                success(f"Found admin panel: {full_url}")
                return
            elif response.status_code == 403:
                info(f"Forbidden (403): {full_url}")
        except requests.RequestException as e:
            error(f"Error checking {full_url}: {e}")

    error("No admin panel found.")
    info("Generating wordlist from webpage content...")
    with open('wordlist.txt', 'w') as f:
        for word in wordlist:
            f.write(word + '\n')
    success("Wordlist generated as 'wordlist.txt'.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Admin Panel Finder Tool')
    parser.add_argument('-u', '--url', help='Website URL (include http:// or https://)', required=True)
    args = parser.parse_args()
    find_admin_panel(args.url)
