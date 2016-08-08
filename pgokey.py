# coding: utf-8

import argparse
from gpsoauth import generate_signature

def init_config():

    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", help="Google Account's User Name or Gmail Address", required=True)
    parser.add_argument("-p", "--password", help="Google Account's Password", required=True)
    parser.add_argument("-o", "--output", help="Output swift code's directory path", required=True)
    config = parser.parse_args()

    return config

def main():
    config = init_config()
    signature = generate_signature(config.username, config.password)
    output = '''
import Foundation

class GoogleAccount {
  static let userName:String = "%(name)s"
  static let password:String = "%(pass)s"
  static let signature:String = "%(signature)s"
}'''%{"name":config.username, "pass":config.password, "signature":signature}
    with open(config.output, "w") as file:
        file.write(output)
    print(config.output + " was generated.(may be) Please check it")

main()
